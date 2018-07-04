#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/27
Desc:   后台管理数据库操作类
"""

import sys
sys.path.append('../')

from util import DbUtil
from util.DateUtil import DateUtil

class AdminDao:
    def __init__(self):
        pass

    # 根据管理员电话号码查询管理员信息
    def queryByTel(self, admin_tel):
        query = 'SELECT * FROM ffstore_admin WHERE admin_tel = "%s" ' % admin_tel
        return DbUtil.query(query)

    # 根据管理员号码和密码查询管理员信息
    def queryByTelAndPwd(self, admin_tel, sms_pwd):
        query = 'SELECT * FROM ffstore_admin WHERE admin_tel = "%s" and sms_pwd = "%s" ' % (admin_tel, sms_pwd)
        return DbUtil.query(query)

    # 更新短信验证码
    def updateSmsPwd(self, admin_tel, sms_pwd):
        current_time = DateUtil().getCurrentTimeStamp()
        update = 'update ffstore_admin set sms_pwd = "%s", login_time = "%s" where admin_tel = "%s"' \
                 % (sms_pwd, current_time, admin_tel)
        return DbUtil.update(update)

    # 更新登录时间(时间戳格式,秒级别)
    def updateLoginTime(self, admin_tel, login_time):
        current_time = DateUtil().getCurrentTimeStamp()
        if not login_time or login_time > current_time:
            return False
        update = 'update ffstore_admin set login_time = "%s" where admin_tel = "%s"' % (login_time, admin_tel)
        return DbUtil.update(update)
