#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : admin management add adverts tornado handler

manager api handler
"""

import sys
sys.path.append('../')
import tornado.web
from constant import ResponseCode
from FFStoreJsonEncoder import *
from net.GetOrder import GetOrder
from util.MD5Util import MD5Util

"""
保存订单信息
请根据请求参数设计接口
"""
class SaveOrderHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)

        # md5Util = MD5Util()
        # if sign == md5Util.md5Signature(time):
        #     getGoods = GetGoods()
        #     netGoodsDetail = getGoods.getGoodsById(goods_id)
        #     baseResponse.code = ResponseCode.op_success
        #     baseResponse.desc = ResponseCode.op_success_desc
        #     baseResponse.data = netGoodsDetail
        # else:
        #     baseResponse.code = ResponseCode.fail_check_api_md5
        #     baseResponse.desc = ResponseCode.fail_check_api_md5_desc
        # json_str = json.dumps(baseResponse, cls=GoodsDetailEncoder)
        # self.write(json_str)
