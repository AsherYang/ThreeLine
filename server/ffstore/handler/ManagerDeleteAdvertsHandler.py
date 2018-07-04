#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/4
Desc:   后台管理系统，删除广告banner handler

manager api handler
"""

import sys
sys.path.append('../')
import tornado.web
from constant import ResponseCode
from FFStoreJsonEncoder import *

from mgrsys.PermissionManager import PermissionManager
from net.GetAdverts import GetAdverts


class ManagerDeleteAdvertsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        sign = self.get_argument('sign', '')
        time = self.get_argument('time', '')
        admin_tel = self.get_argument('tel', '')
        sms_pwd = self.get_argument('sms', '')

        delete_Id = self.get_argument('adverts_id')

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            getAdverts = GetAdverts()
            deleteResult = getAdverts.deleteAdvertsById(delete_Id)
            if deleteResult:
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.code = ResponseCode.fail_op_db_data
                baseResponse.desc = ResponseCode.fail_op_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
