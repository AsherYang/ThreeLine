#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : UID tornado request handler

api handler
"""
import sys
sys.path.append('../')

import tornado.web
from util.GenerateIDUtil import GenerateIDUtil
from constant import ResponseCode
from BaseResponse import BaseResponse
from FFStoreJsonEncoder import *

# 生成唯一的ID
class GetUIDHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        generateIdUtil = GenerateIDUtil()
        uid = generateIdUtil.getUID()
        baseResponse = BaseResponse()
        if uid:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = str(uid)
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
