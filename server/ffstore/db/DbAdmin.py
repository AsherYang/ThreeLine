#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/27
Desc  : 管理员类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
admin_tel VARCHAR(20) NOT NULL UNIQUE,
sms_pwd VARCHAR(50),
login_time VARCHAR(20)
"""


class DbAdmin:

    def __init__(self):
        self._admin_tel = None
        self._sms_pwd = None
        self._login_time = None

    @property
    def admin_tel(self):
        return self._admin_tel

    @admin_tel.setter
    def admin_tel(self, value):
        self._admin_tel = value

    @property
    def sms_pwd(self):
        return self._sms_pwd

    @sms_pwd.setter
    def sms_pwd(self, value):
        self._sms_pwd = value

    @property
    def login_time(self):
        return self._login_time

    @login_time.setter
    def login_time(self, value):
        self._login_time = value
