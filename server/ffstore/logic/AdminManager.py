#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/27
Desc  : 系统后台管理类
"""

import sys
sys.path.append('../')

from db.DbAdmin import DbAdmin
from db.AdminDao import AdminDao
from constant import LoginStatus
from util.DateUtil import DateUtil

# 有效登录时长(1天)
LOGIN_TIME_INTERVAL = 86400


class AdminManager:

    def __init__(self):
        self.adminDao = AdminDao()
        self.dateUtil = DateUtil()

    """
    校验登陆信息, 
    1. 检验用户号码和密码
    2. 检验登录实效，超期操作非法。
    只有当查询到管理员数据，以及管理员号码不为空时，校验通过。
    """
    def checkLoginState(self, admin_tel, sms_pwd):
        dbAdmin = self.getAdminByTelAndPwd(admin_tel, sms_pwd)
        if not dbAdmin:
            return LoginStatus.STATUS_LOGIN_NO_ADMIN
        dbLoginTime = dbAdmin.login_time
        currentTime = self.dateUtil.getCurrentTimeStamp()
        if not dbLoginTime or dbLoginTime + LOGIN_TIME_INTERVAL <= currentTime:
            return LoginStatus.STATUS_LOGIN_OUT_OF_DATE
        return LoginStatus.STATUS_LOGIN_SUCCESS

    def getAdminByTelAndPwd(self, admin_tel, sms_pwd):
        if not admin_tel or not sms_pwd:
            return None
        adminResult = self.adminDao.queryByTelAndPwd(admin_tel, sms_pwd)
        return self.convertDbRow2Admin(adminResult)

    """
    更新登录密码, 该密码会以短信形式发送到手机, 以及微信通知
    """
    def updateLoginPwd(self, admin_tel, sms_pwd):
        return self.adminDao.updateSmsPwd(admin_tel, sms_pwd)

    """
    将登录时间更新为当前时间
    """
    def updateLoginTime2Current(self, admin_tel):
        currentTime = self.dateUtil.getCurrentTimeStamp()
        return self.adminDao.updateLoginTime(admin_tel, currentTime)

    # =========================== 转换开始 ===================================== #
    # 将数据库查询出来的结果，对应设置给admin实体bean, 并将单个 admin 返回出去
    def convertDbRow2Admin(self, dbAdminRowsResult):
        if not dbAdminRowsResult:
            return None
        dbAdmin = DbAdmin()
        row_id = dbAdminRowsResult[0]
        dbAdmin.admin_name = dbAdminRowsResult[1]
        dbAdmin.sms_pwd = dbAdminRowsResult[2]
        dbAdmin.admin_tel = dbAdminRowsResult[3]
        dbAdmin.login_time = dbAdminRowsResult[4]
        return dbAdmin

    # =========================== 转换结束 ===================================== #