#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : 搜索商品列表 tornado handler

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
搜索商品
接口与返回值和 {@see getHostGoodsListHandler} 类似

https://sujiefs.com//api/mall/searchGoodsList?page=1&size=10&searchKeyWords=&cateCode=008005&sort=-1&skuval=&sign=d2ebecbb0a1c36b51b0b5a20a6a85588&time=20180610132307
"""
class SearchGoodsListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        searchKeywords = self.get_argument('searchKeyWords')
        cateCode = self.get_argument('cateCode')
        sort = self.get_argument('sort')
        skuval = self.get_argument('skuval')
        getGoods = GetGoods()
        netSearchGoods = getGoods.getSearchGoodsList(searchKeywords, cateCode, skuval, page, size, sort)
        baseResponse = BaseResponse()
        if netSearchGoods:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            searchGoodsCount = getGoods.getGoodsCountByKeywords(searchKeywords, cateCode, skuval)
            page_total = (searchGoodsCount / size) + (1 if searchGoodsCount % size > 0 else 0)
            baseResponse.pageNum = page
            baseResponse.pageSize = size
            baseResponse.page_total = page_total
            baseResponse.totalCount = searchGoodsCount
            baseResponse.data = netSearchGoods
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=HostGoodsEncoder)
        self.write(json_str)
        pass

