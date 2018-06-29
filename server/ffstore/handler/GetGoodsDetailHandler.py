#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : get goods detail tornado handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web

from BaseResponse import BaseResponse
from constant import ResponseCode
from FFStoreJsonEncoder import *
from net.GetGoods import GetGoods


"""
获取商品详情信息
https://sujiefs.com//api/mall/goods?id=2c9257a16136c3d6016348cc332b5e5d&sign=d1260c4c7c83415023bccdcc6b69f293&time=20180606221032
"""
class GetGoodsDetailHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        goods_id = self.get_argument('id')
        getGoods = GetGoods()
        netGoodsDetail = getGoods.getGoodsById(goods_id)
        baseResponse = BaseResponse()
        if netGoodsDetail:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = netGoodsDetail
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=GoodsDetailEncoder)
        self.write(json_str)
