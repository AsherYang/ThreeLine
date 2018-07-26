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
from constant import ResponseCode
from FFStoreJsonEncoder import *

from net.GetAdverts import GetAdverts
from net.NetAdverts import NetAdverts
from util.DateUtil import DateUtil
from mgrsys.PermissionManager import PermissionManager


"""
添加广告接口
用于后台添加厂家管理
管理员操作，注意需要严格的权限验证。
"""
class ManagerAddBrandHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        sign = param['sign']
        time = param['time']
        admin_tel = param['tel']
        sms_pwd = param['sms']

        brand_name = param['brand_name']
        brand_logo = param['brand_logo']

        getAdverts = GetAdverts()
        netAdverts = NetAdverts()
        netAdverts.title = advert_title
        netAdverts.picUrl = advert_pic_url
        netAdverts.sort = advert_sort
        netAdverts.createTime = DateUtil().getCurrentTime()

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time, admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            addResult = getAdverts.addAdverts(netAdverts, advert_cate_id)
            if addResult:
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.code = ResponseCode.fail_op_db_data
                baseResponse.desc = ResponseCode.fail_op_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
