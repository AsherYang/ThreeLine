#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/27
Desc  : 管理员类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
admin_name VARCHAR(50),
sms_pwd VARCHAR(50),
admin_tel VARCHAR(20) NOT NULL UNIQUE,
login_time VARCHAR(20)
"""


class DbAdmin:

    def __init__(self):
        pass

    @property
    def admin_name(self):
        return self.admin_name

    @property
    def admin_name(self, value):
        self.admin_name = value

    @property
    def sms_pwd(self):
        return self.sms_pwd

    @property
    def sms_pwd(self, value):
        self.sms_pwd = value

    @property
    def admin_tel(self):
        return self.admin_tel

    @property
    def admin_tel(self, value):
        self.admin_tel = value

    @property
    def login_time(self):
        return self.login_time

    @property
    def login_time(self, value):
        self.login_time = value