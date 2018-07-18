#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : 更新用户消费记录 tornado handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web
from net.GetUser import GetUser
from constant import ResponseCode
from BaseResponse import BaseResponse
from FFStoreJsonEncoder import *


"""
更新用户消费数据
"""
class UpdateUserCostHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        phone = param['phone']
        cost = param['cost_this_time']
        result = GetUser().updateUserCost(phone, cost)
        # todo
        if result:
            print 'add user cost successfully!'
        else:
            print ResponseCode.add_user_cost_error_desc