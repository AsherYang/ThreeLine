#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : delete category and the category goods tornado handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web
from net.GetGoods import GetGoods
from constant import ResponseCode
from BaseResponse import BaseResponse
from FFStoreJsonEncoder import *


# 删除商品分类，及该分类下的所有商品
class ManagerDeleteCateAndGoodsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        cate_id = self.get_argument('cate_id', '')
        getGoods = GetGoods()
        deleteResult = getGoods.deleteCateAndGoods(cate_id)
        baseResponse = BaseResponse()
        if deleteResult:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
