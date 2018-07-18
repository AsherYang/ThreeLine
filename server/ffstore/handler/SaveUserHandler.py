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
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        userName = param['name']
        phone = param['phone']
        address = param['address']
        user = DbUser()
        user.user_name = userName
        user.user_tel = phone
        user.address = address

        baseResponse = BaseResponse()
        if not phone:
            baseResponse.code = ResponseCode.invalid_user_phone
            baseResponse.desc = ResponseCode.invalid_user_phone_desc
        else:
            result = GetUser().operateUser2Db(user)
            if result:
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.code = ResponseCode.fail_update_user_info
                baseResponse.desc = ResponseCode.fail_update_user_info_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
