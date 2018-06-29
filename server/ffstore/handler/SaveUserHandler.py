#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : 保存用户信息 tornado handler

api handler
"""

import sys
sys.path.append('../')
import tornado.web
from net.GetUser import GetUser
from constant import ResponseCode
from BaseResponse import BaseResponse
from FFStoreJsonEncoder import *
from db.DbUser import DbUser


"""
save user to db
"""
class SaveUserHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        userName = self.get_argument('name', '')
        phone = self.get_argument('phone', '')
        address = self.get_argument('address', '')
        user = DbUser()
        user.user_name = userName
        user.user_tel = phone
        user.address = address
        result = GetUser().operateUser2Db(user)
        baseResponse = BaseResponse()
        if result:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
        elif not phone:
            baseResponse.code = ResponseCode.invalid_user_phone
            baseResponse.desc = ResponseCode.invalid_user_phone_desc
        elif not address:
            baseResponse.code = ResponseCode.invalid_user_address
            baseResponse.desc = ResponseCode.invalid_user_address_desc
        else:
            baseResponse.code = ResponseCode.update_user_info_error
            baseResponse.desc = ResponseCode.update_user_info_error_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
