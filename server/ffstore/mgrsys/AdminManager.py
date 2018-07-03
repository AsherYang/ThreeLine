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
from RandomPwd import RandomPwd
from mgrsys.NotifyAdmin import NotifyAdmin, SMS_SUBJECT_INVALID_ADMIN_LOGIN

# 有效登录时长(1天)
LOGIN_TIME_INTERVAL = 86400


class AdminManager:

    def __init__(self):
        self.adminDao = AdminDao()
        self.dateUtil = DateUtil()
        self.notifyAdmin = NotifyAdmin()

    """
    登录
    1. 如果数据库中没有对应的管理员手机号, 禁止非法登录
    2. 如果没有短信验证码, 或者验证码过期, 则重新发送验证码到手机
    3. 根据新验证码重新登录管理系统
    4. 登录成功后，需要运维将管理员登录信息短信或微信告知我这个超管
    """
    def login(self, admin_tel, sms_pwd):
        login_status = self.checkLoginState(admin_tel, sms_pwd)
        if login_status == LoginStatus.STATUS_LOGIN_NO_ADMIN:
            # 警告！非法管理员操作
            sms_msg = '%s : 正在登陆后台系统, 请注意检查! ' % admin_tel
            self.notifyAdmin.sendMsg(sms_msg=sms_msg, subject=SMS_SUBJECT_INVALID_ADMIN_LOGIN)
            return False
        elif login_status == LoginStatus.STATUS_LOGIN_FAIL_PWD or login_status == LoginStatus.STATUS_LOGIN_OUT_OF_DATE:
            # 重新发送验证码到手机进行登录
            pwd = self.getSmsPwdAndSaveDb(admin_tel)
            if not pwd:
                return False
            # 发送至当前管理员手机
            # todo , 发送短信验证码
            # 需要重新登录, 所以返回false
            return False
        elif login_status == LoginStatus.STATUS_LOGIN_SUCCESS:
            # 发送运维信息，告诉我这个超管，有人登录系统了
            # todo
            return True
        else:
            return False


    """
    获取短信验证码, 获取短信验证码后，需要更新当前最新的验证码到数据库中
    """
    def getSmsPwdAndSaveDb(self, admin_tel):
        if not admin_tel:
            return None
        pwd = RandomPwd().genPwd()
        updateResult = self.adminDao.updateSmsPwd(admin_tel, pwd)
        if updateResult:
            return pwd
        return None

    """
    校验登陆信息, 
    1. 检验用户号码和密码
    2. 检验登录实效，超期操作非法。
    只有当查询到管理员数据，以及管理员号码不为空时，校验通过。
    """
    def checkLoginState(self, admin_tel, sms_pwd):
        dbAdmin = self.getAdminByTel(admin_tel)
        if not dbAdmin:
            return LoginStatus.STATUS_LOGIN_NO_ADMIN
        dbAdmin = self.getAdminByTelAndPwd(admin_tel, sms_pwd)
        if not dbAdmin:
            return LoginStatus.STATUS_LOGIN_FAIL_PWD
        dbLoginTime = dbAdmin.login_time
        currentTime = self.dateUtil.getCurrentTimeStamp()
        if not dbLoginTime or dbLoginTime + LOGIN_TIME_INTERVAL <= currentTime:
            return LoginStatus.STATUS_LOGIN_OUT_OF_DATE
        return LoginStatus.STATUS_LOGIN_SUCCESS

    """
    查询数据库, 根据管理员号码查询管理员信息
    该操作，用于前期判断是否存在该管理员，若不存在, 禁止非法操作, 同时不进行发短信验证码功能
    """
    def getAdminByTel(self, admin_tel):
        if not admin_tel:
            return None
        adminResult = self.adminDao.queryByTel(admin_tel)
        return self.convertDbRow2Admin(adminResult)

    """
    查询数据库, 根据管理员号码和密码查询管理员信息
    该操作可用于登录校验，满足查询的结果，说明已经获取到短信验证码了
    """
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