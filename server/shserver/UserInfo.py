#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2017/11/29
Desc  : UserInfo: userName|phone|address
"""
import DbUtil

class User():
    @property
    def userName(self):
        return self.userName

    @property
    def userName(self, value):
        self.userName = value

    @property
    def phone(self):
        return self.phone

    @property
    def phone(self, value):
        self.phone = value

    @property
    def address(self):
        return self.address

    @property
    def address(self, value):
        self.address = value


# 数据库操作
class operateDb():

    def saveToDb(self, userInfo):
        if isinstance(userInfo, User):
            insert = 'insert into sh_user (userName, userTel, userAddress) values("%s", "%s", "%s")' \
                     % (userInfo.userName, userInfo.phone, userInfo.address)
            DbUtil.insert(insert)


