#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : 获取商品 tornado handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web
from BaseResponse import BaseResponse
from FFStoreJsonEncoder import *
from net.GetGoods import GetGoods


"""
get all goods
"""
class GetAllGoodsHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        getGoods = GetGoods()
        # todo getAllGoods
        allGoodsList = getGoods.getAllGoods()
        baseResponse = BaseResponse()
        baseResponse.code = "000001"
        baseResponse.desc = "successfully"
        for goods in allGoodsList:
            baseResponse.data.append(goods)
        json_str = json.dumps(baseResponse, cls=AllGoodsEncoder)
        self.write(json_str)
