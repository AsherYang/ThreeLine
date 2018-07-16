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
from util.LogUtil import LogUtil
from mgrsys.NotifyAdmin import *


class ManagerAdminLoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        logging = LogUtil().getLogging()
        param = self.request.body.decode('utf-8')
        prarm = json.loads(param)
        sign = prarm['sign']
        time = prarm['time']
        admin_tel = prarm['tel']
        sms_pwd = prarm['sms']

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        logging.info('baseResponse code: ', baseResponse.code)
        # 登录还在有效期内。
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            # 登录成功
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = u'恭喜! 系统登陆成功.'
            # 通知超管(我)
            admin_sms_msg = '用户 {tel} 已成功登陆后台系统.'.format(tel=admin_tel)
            notifyAdmin = NotifyAdmin()
            notifyAdmin.sendMsg(sms_msg=admin_sms_msg, subject=SMS_SUBJECT_LOGIN)
            notifyAdmin.sendWxMsg(msg=admin_sms_msg)
        elif baseResponse.code == ResponseCode.fail_admin_out_of_date \
                or baseResponse.code == ResponseCode.fail_admin_login:
            adminMgr = AdminManager()
            loginResult = adminMgr.login(admin_tel=admin_tel, sms_pwd=sms_pwd)
            if loginResult:
                baseResponse.data = u'您已成功登录!'
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.data = u'新密码已发送至手机, 请按新密码重新登录。'
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)



