#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/4
Desc:   后台管理员登录后台系统

manager api handler
"""

import sys
sys.path.append('../')
import tornado.web
from constant import ResponseCode
from FFStoreJsonEncoder import *
from mgrsys.AdminManager import AdminManager
from mgrsys.PermissionManager import PermissionManager


class ManagerAdminLoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        sign = self.get_argument('sign', '')
        time = self.get_argument('time', '')
        admin_tel = self.get_argument('tel', '')
        sms_pwd = self.get_argument('sms', '')

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        # 登录还在有效期内。
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            # 登录成功
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
        elif baseResponse.code == ResponseCode.fail_admin_out_of_date \
                or baseResponse.code == ResponseCode.fail_admin_login:
            adminMgr = AdminManager()
            loginResult = adminMgr.login(admin_tel=admin_tel, sms_pwd=sms_pwd)
            if loginResult:
                baseResponse.data = u'您已成功登录！'
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.data = u'新密码已发送至手机, 请按新密码重新登录。'
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)



