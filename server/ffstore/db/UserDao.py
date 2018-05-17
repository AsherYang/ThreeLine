#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   操作用户数据库DAO 类
"""

from DbUser import DbUser
from ffstore.util import NumberUtil
from ffstore.util import DbUtil


class UserDao:
    def __init__(self):
        pass

    def saveToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            insert = 'insert into ffstore_user (user_name, user_tel, user_address, buy_times, cost_count) values("%s", "%s", "%s", "%d", "%d")' \
                     % (userInfo.user_name, userInfo.user_tel, userInfo.user_address, userInfo.buy_times,
                        userInfo.cost_count)
            print 'insert user to db.'
            return DbUtil.insert(insert)
        return False

    def updateToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            if not userInfo.user_tel:
                return False
            if not userInfo.user_name:
                return self.updateAddressToDb(userInfo)
            elif not userInfo.user_address:
                return self.updateNameToDb(userInfo)
            else:
                update = 'update ffstore_user set user_name = "%s", user_address = "%s" where user_tel = "%s" ' \
                         % (userInfo.user_name, userInfo.user_address, userInfo.user_tel)
                print 'update user name and address to db'
                return DbUtil.update(update)
        return False

    def updateAddressToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            update = 'update ffstore_user set user_address = "%s" where user_tel = "%s" ' \
                     % (userInfo.user_address, userInfo.user_tel)
            print 'update user address to db'
            return DbUtil.update(update)
        return False

    def updateNameToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            update = 'update ffstore_user set user_name = "%s" where user_tel = "%s" ' \
                     % (userInfo.user_name, userInfo.user_tel)
            print 'update user name and address to db'
            return DbUtil.update(update)
        return False

    def updateUserCost(self, userInfo, costThisTime):
        if not NumberUtil.is_number(costThisTime):
            return False
        if isinstance(userInfo, DbUser):
            userTmp = self.queryFromDb(userInfo)
            if userTmp:
                cost_count = userTmp.cost_count + costThisTime
                buy_times = userTmp.buy_times + 1
                update = 'update ffstore_user set buy_times = "%d", cost_count = "%d" where user_tel = "%s" ' \
                         % (buy_times, cost_count, userInfo.user_tel)
                return DbUtil.update(update)
        return False

    def queryFromDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            query = 'select * from ffstore_user where user_tel = "%s" ' % userInfo.user_tel
            return DbUtil.query(query)
        return None

    def deleteFromDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            delete = 'delete from ffstore_user where user_tel = "%s" ' % userInfo.user_tel
            print 'delete user:%s from db.' % userInfo.user_tel
            return DbUtil.delete(delete)
        return False

    # 数据库操作，先查用户信息，没查到插入，查到就更新
    def operate(self, userInfo):
        if isinstance(userInfo, DbUser):
            user = self.queryFromDb(userInfo)
            if user:
                return self.updateToDb(userInfo)
            else:
                return self.saveToDb(userInfo)
        print "save to db is not user bean."
        return False
