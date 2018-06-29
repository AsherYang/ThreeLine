#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : get host goods list tornado handler

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
点击封面列表进入的分类展示专区
分类列表，拿到的数据是 goods 表中对应cate_code 字段的数据
sort: 排序字段，根据 "综合","销量","价格"排序
skuval: "尺码"
https://sujiefs.com//api/home/hostGoodsList?page=1&size=10&cateCode=021&sort=1&skuval=&sign=694e9f6dec1f1d11475a5ac688d8d644&time=20180430155433
"""
class GetHostGoodsListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        cateCode = self.get_argument('cateCode')
        sort = int(self.get_argument('sort'))
        skuval = self.get_argument('skuval')
        getGoods = GetGoods()
        netHostGoods = getGoods.getHostGoods(cateCode, skuval, page, size, sort)
        baseResponse = BaseResponse()
        if netHostGoods:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            hostGoodsCount = getGoods.getGoodsCountByCate(cateCode, skuval)
            page_total = (hostGoodsCount / size) + (1 if hostGoodsCount % size > 0 else 0)
            baseResponse.pageNum = page
            baseResponse.pageSize = size
            baseResponse.page_total = page_total
            baseResponse.totalCount = hostGoodsCount
            baseResponse.data = netHostGoods
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=HostGoodsEncoder)
        self.write(json_str)
