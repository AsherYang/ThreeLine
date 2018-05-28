#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   json encoder for custom class
"""

import json
from BaseResponse import BaseResponse
from ffstore.net.NetCategory import NetCategory
from ffstore.net.NetDiscover import NetDiscover
from db.DbGoods import DbGoods

"""
将Category 转成 Json 字符串
"""
class CategoryEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseResponse):
            contentData = obj.data
            # print type(contentData)
            realContent = []
            if isinstance(contentData, list):
                for data in contentData:
                    if isinstance(data, NetCategory):
                        string = {'id': data.id, 'code': data.code, 'name': data.name, 'logo': data.logo,
                                  'parent_code': data.parent_code}
                        realContent.append(string)
            elif isinstance(contentData, basestring):
                realContent = contentData
            else:
                realContent.append('unknown data type')
            return {'code': obj.code, 'desc': obj.desc,
                    'result': realContent}
            # if isinstance(contentData, list):
            #     print contentData[0].author
            # else:
            #     print type(contentData)
        else:
            return json.JSONEncoder.default(self, obj)


"""
将goods 转成 Json 字符串
"""
class AllGoodsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseResponse):
            contentData = obj.data
            # print type(contentData)
            realContent = []
            if isinstance(contentData, list):
                for data in contentData:
                    if isinstance(data, DbGoods):
                        string = {'cate_id': data.cate_id, 'cate_name': data.cate_name, 'itemid': data.itemid,
                                  'item_desc': data.item_desc, 'item_name': data.item_name, 'imgs': data.imgs,
                                  'price': data.price, 'update_time': data.update_time}
                        realContent.append(string)
            elif isinstance(contentData, basestring):
                realContent = contentData
            else:
                realContent.append('unknown data type')
            return {'code': obj.code, 'desc': obj.desc,
                    'result': realContent}
            # if isinstance(contentData, list):
            #     print contentData[0].author
            # else:
            #     print type(contentData)
        else:
            return json.JSONEncoder.default(self, obj)

"""
将HomeDiscover 转成 Json 字符串
"""
class HomeDiscoverEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseResponse):
            contentData = obj.data
            # print type(contentData)
            realContent = []
            if isinstance(contentData, list):
                for data in contentData:
                    if isinstance(data, NetDiscover):
                        string = {'id': data.id, 'code': data.code, 'logo': data.logo,
                                  'attr_brand_name': data.attr_brand_name,
                                  'attr_market_year': data.attr_market_year }
                        realContent.append(string)
            elif isinstance(contentData, basestring):
                realContent = contentData
            else:
                realContent.append('unknown data type')
            return {'code': obj.code, 'desc': obj.desc,
                    'result': realContent}
            # if isinstance(contentData, list):
            #     print contentData[0].author
            # else:
            #     print type(contentData)
        else:
            return json.JSONEncoder.default(self, obj)


"""
将string 转成 Json 字符串
"""
class StrEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseResponse):
            contentData = obj.data
            # print type(contentData)
            realContent = []
            if isinstance(contentData, basestring):
                realContent = contentData
            else:
                realContent.append(' ')
            return {'code': obj.code, 'desc': obj.desc,
                    'result': realContent}
        else:
            return json.JSONEncoder.default(self, obj)