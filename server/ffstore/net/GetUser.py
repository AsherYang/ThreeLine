#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/6
Desc  : get user 获取用户接口，返回网络数据
"""

import sys
sys.path.append('../')

from db.UserDao import UserDao


class GetUser:
    def __init__(self):
        pass

    # 保存或者更新用户进数据库
    def operateUser2Db(self, dbUser):
        if not dbUser:
            return False
        elif not dbUser.user_tel:
            return False
        else:
            return UserDao().operate(dbUser)

    # 更新用户消费
    def updateUserCost(self, user_tel, costThisTime=0):
        if not user_tel:
            return False
        else:
            return UserDao().updateUserCost(user_tel, costThisTime)
