#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   操作用户数据库DAO 类
"""
import sys
sys.path.append('../')

from DbUser import DbUser
from util import NumberUtil
from util import DbUtil


class UserDao:
    def __init__(self):
        pass

    def saveToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            insert = 'insert into ffstore_user (user_id, user_name, user_tel, user_address, buy_times, cost_count)' \
                     ' values("%s", "%s", "%s", "%s", "%d", "%d")' \
                     % (userInfo.user_id, userInfo.user_name, userInfo.user_tel, userInfo.user_address,
                        userInfo.buy_times, userInfo.cost_count)
            print 'insert user to db.'
            return DbUtil.insert(insert)
        return False

    # 更新用户信息，会更新所有用户字段，如果需要更新单个字段值，请使用单个更新的方式
    def updateToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            update = 'update ffstore_user set user_name = "%s", user_address = "%s", user_tel = "%s" where user_id = "%s" ' \
                     % (userInfo.user_name, userInfo.user_address, userInfo.user_tel, userInfo.user_id)
            print 'update user name and address to db'
            return DbUtil.update(update)
        return False

    def updateAddressToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            update = 'update ffstore_user set user_address = "%s" where user_id = "%s" ' \
                     % (userInfo.user_address, userInfo.user_id)
            print 'update user address to db'
            return DbUtil.update(update)
        return False

    def updateNameToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            update = 'update ffstore_user set user_name = "%s" where user_id = "%s" ' \
                     % (userInfo.user_name, userInfo.user_id)
            print 'update user name and address to db'
            return DbUtil.update(update)
        return False

    def updateTelToDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            update = 'update ffstore_user set user_tel = "%s" where user_id = "%s" ' \
                     % (userInfo.user_tel, userInfo.user_id)
            print 'update user tel and address to db'
            return DbUtil.update(update)
        return False

    def updateUserCost(self, user_tel, costThisTime):
        if not NumberUtil.is_number(costThisTime):
            return False
        userTmp = self.queryByUserTel(user_tel)
        if userTmp:
            cost_count = userTmp.cost_count + costThisTime
            buy_times = userTmp.buy_times + 1
            update = 'update ffstore_user set buy_times = "%d", cost_count = "%d" where user_id = "%s" ' \
                     % (buy_times, cost_count, userTmp.user_id)
            return DbUtil.update(update)
        return False

    def queryFromDb(self, userInfo):
        if isinstance(userInfo, DbUser):
            query = 'select * from ffstore_user where user_id = "%s" ' % userInfo.user_id
            return DbUtil.query(query)
        return None

    def queryByUserId(self, user_id):
        if not user_id:
            return None
        query = 'select * from ffstore_user where user_id = "%s" ' % user_id
        return DbUtil.query(query)

    def queryByUserTel(self, user_tel):
        if not user_tel:
            return None
        query = 'select * from ffstore_user where user_tel = "%s" ' % user_tel
        return DbUtil.query(query)

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
