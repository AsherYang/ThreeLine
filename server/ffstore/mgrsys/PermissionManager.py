#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/2
Desc:   权限管理类

主要做一些权限校验
"""

from BaseResponse import BaseResponse
from constant import ResponseCode
from constant import LoginStatus
from util.MD5Util import MD5Util, ADMIN_SECRET_KEY
from mgrsys.AdminManager import AdminManager


class PermissionManager:

    def __init__(self):
        pass

    """
    校验管理员权限
    1. 先根据时间做一次md5 校验
    2. 再根据用户号码和密码做一次登录校验
    3. 最后校验登陆时效（第3与2步在adminMgr.checkLoginState中）
    登录过的管理员才有操作权限
    @:return baseResponse 用于直接在 api 中返回
    """
    def checkAdminPermissionWithLoginStatus(self, sign, time, admin_tel, sms_pwd):
        baseResponse = BaseResponse()
        if sign is None or time is None or admin_tel is None or sms_pwd is None:
            baseResponse.code = ResponseCode.fail_api_args
            baseResponse.desc = ResponseCode.fail_api_args_desc
        else:
            md5Util = MD5Util(ADMIN_SECRET_KEY)
            adminMgr = AdminManager()
            if sign == md5Util.md5Signature(time):
                login_status = adminMgr.checkLoginState(admin_tel, sms_pwd)
                if login_status == LoginStatus.STATUS_LOGIN_SUCCESS:
                    baseResponse.code = ResponseCode.success_check_admin_permission
                    baseResponse.desc = ResponseCode.success_check_admin_permission_desc
                elif login_status == LoginStatus.STATUS_LOGIN_OUT_OF_DATE:
                    baseResponse.code = ResponseCode.fail_admin_out_of_date
                    baseResponse.desc = ResponseCode.fail_admin_out_of_date_desc
                else:
                    baseResponse.code = ResponseCode.fail_admin_login
                    baseResponse.desc = ResponseCode.fail_admin_login_desc
            else:
                baseResponse.code = ResponseCode.illegal_md5_client
                baseResponse.desc = ResponseCode.illegal_md5_client_desc
        return baseResponse
