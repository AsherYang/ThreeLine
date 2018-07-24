#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : get my order list tornado handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web
from BaseResponse import BaseResponse
from constant import ResponseCode
from FFStoreJsonEncoder import *
from util.MD5Util import MD5Util
from net.GetOrder import GetOrder


"""
获取全部订单总数
https://sujiefs.com//api/mall/goodsOrder/getMyOrderSize?openId=oeuj50KHMqsh5kYZYWQJuwmY5yG0&sign=c1cc2cc92f2553ab382d612bb6c379b2&time=20180611214443
"""
class GetMyOrderSizeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        userId = self.get_argument('openId')
        md5Util = MD5Util()
        baseResponse = BaseResponse()
        if sign == md5Util.md5Signature(time):
            getOrder = GetOrder()
            orderSize = getOrder.getMyOrderSize(userId)
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = orderSize
        else:
            baseResponse.code = ResponseCode.fail_check_api_md5
            baseResponse.desc = ResponseCode.fail_check_api_md5_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
