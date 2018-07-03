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
from util.MD5Util import MD5Util


"""
获取商品详情信息
https://sujiefs.com//api/mall/goods?id=2c9257a16136c3d6016348cc332b5e5d&sign=d1260c4c7c83415023bccdcc6b69f293&time=20180606221032
"""
class GetGoodsDetailHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        goods_id = self.get_argument('id')
        baseResponse = BaseResponse()
        md5Util = MD5Util()
        if sign == md5Util.md5Signature(time):
            getGoods = GetGoods()
            netGoodsDetail = getGoods.getGoodsById(goods_id)
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = netGoodsDetail
        else:
            baseResponse.code = ResponseCode.fail_check_api_md5
            baseResponse.desc = ResponseCode.fail_check_api_md5_desc
        json_str = json.dumps(baseResponse, cls=GoodsDetailEncoder)
        self.write(json_str)
