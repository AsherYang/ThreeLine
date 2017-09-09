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
from Category import Category
from Goods import Goods

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
                    if isinstance(data, Category):
                        string = {'cate_id': data.cate_id, 'cate_name': data.cate_name, 'parent_id': data.parent_id,
                                  'parent_cate_name': data.parent_cate_name, 'sort_num': data.sort_num, 'cate_item_num': data.cate_item_num,
                                  'description': data.description, 'listUrl': data.listUrl, 'shopName': data.shopName,
                                  'shopLogo': data.shopLogo, 'update_time': data.update_time}
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
                    if isinstance(data, Goods):
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