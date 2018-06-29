#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : get category handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web
from BaseResponse import BaseResponse
from FFStoreJsonEncoder import *

from net.GetCategory import GetCategory


"""
get category
获取所有的分类，包括一级分类和二级分类
"""
class GetCategoryHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        getCategory = GetCategory()
        categoryList = getCategory.doGetCategory()
        baseResponse = BaseResponse()
        if categoryList:
            for category in categoryList:
                baseResponse.data.append(category)
        json_str = json.dumps(baseResponse, cls=CategoryEncoder)
        self.write(json_str)