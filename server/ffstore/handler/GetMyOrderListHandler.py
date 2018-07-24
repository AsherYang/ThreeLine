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
获取订单信息
根据不同的参数，返回不同的值
https://sujiefs.com//api/mall/goodsOrder/getMyOrderList?openId=oeuj50KHMqsh5kYZYWQJuwmY5yG0&orderStatus=&receiveFlg=0&page=1&size=10&type=1&sign=c1cc2cc92f2553ab382d612bb6c379b2&time=20180611214443
"""
class GetMyOrderListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        userId = self.get_argument('openId')
        type = self.get_argument('type')
        receiveFlg = int(self.get_argument('receiveFlg'))
        orderStatus = self.get_argument('orderStatus')
        md5Util = MD5Util()
        baseResponse = BaseResponse()
        if sign == md5Util.md5Signature(time):
            getOrder = GetOrder()
            netOrders = getOrder.getMyOrderList(userId, orderStatus, page, size)
            if netOrders:
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
                # todo
                # hostGoodsCount = getGoods.getGoodsCountByCate(cateCode, skuval)
                # page_total = (hostGoodsCount / size) + (1 if hostGoodsCount % size > 0 else 0)
                # baseResponse.pageNum = page
                # baseResponse.pageSize = size
                # baseResponse.page_total = page_total
                # baseResponse.totalCount = hostGoodsCount
                # baseResponse.data = netHostGoods
            else:
                baseResponse.code = ResponseCode.op_fail
                baseResponse.desc = ResponseCode.op_fail_desc
        else:
            baseResponse.code = ResponseCode.fail_check_api_md5
            baseResponse.desc = ResponseCode.fail_check_api_md5_desc
        json_str = json.dumps(baseResponse, cls=HostGoodsEncoder)
        self.write(json_str)
