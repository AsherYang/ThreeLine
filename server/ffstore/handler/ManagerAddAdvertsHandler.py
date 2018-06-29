#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : admin management add adverts tornado handler

manager api handler
"""

import sys
sys.path.append('../')
import tornado.web
from BaseResponse import BaseResponse
from constant import ResponseCode
from FFStoreJsonEncoder import *

from net.GetAdverts import GetAdverts
from net.NetAdverts import NetAdverts
from util.DateUtil import DateUtil
from mgrsys.AdminManager import AdminManager
from util.MD5Util import MD5Util, ADMIN_SECRET_KEY
from constant import LoginStatus


"""
添加广告接口
用于后台banner管理
1. 先根据时间做一次md5 校验
2. 再根据用户号码和密码做一次登录校验
3. 最后校验登陆时效
"""
class ManagerAddAdvertsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        sign = self.get_argument('sign', '')
        time = self.get_argument('time', '')
        admin_tel = self.get_argument('tel', '')
        sms_pwd = self.get_argument('sms', '')
        advert_cate_id = self.get_argument('cate_id', '')
        advert_title = self.get_argument('title', '')
        advert_sort = self.get_argument('sort', -1)
        advert_pic_url = self.get_argument('pic_url', '')
        baseResponse = BaseResponse()
        md5Util = MD5Util(ADMIN_SECRET_KEY)
        adminMgr = AdminManager()
        getAdverts = GetAdverts()
        netAdverts = NetAdverts()
        netAdverts.title = advert_title
        netAdverts.picUrl = advert_pic_url
        netAdverts.sort = advert_sort
        netAdverts.createTime = DateUtil().getCurrentTime()
        if sign == md5Util.md5Signature(time):
            login_status = adminMgr.checkLoginState(admin_tel, sms_pwd)
            if login_status == LoginStatus.STATUS_LOGIN_SUCCESS:
                addResult = getAdverts.addAdverts(netAdverts, advert_cate_id)
                if not addResult:
                    baseResponse.code = ResponseCode.op_fail
                    baseResponse.desc = ResponseCode.op_fail_desc
                else:
                    baseResponse.code = ResponseCode.op_success
                    baseResponse.desc = ResponseCode.op_success_desc
            elif login_status == LoginStatus.STATUS_LOGIN_OUT_OF_DATE:
                baseResponse.code = ResponseCode.fail_user_out_of_date
                baseResponse.desc = ResponseCode.fail_user_out_of_date_desc
            else:
                baseResponse.code = ResponseCode.fail_user_login
                baseResponse.desc = ResponseCode.fail_user_login_desc
        else:
            baseResponse.code = ResponseCode.illegal_md5_client
            baseResponse.desc = ResponseCode.illegal_md5_client_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
