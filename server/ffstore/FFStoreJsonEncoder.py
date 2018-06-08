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
from ffstore.net.NetHostGoods import NetHostGoods
from db.DbGoods import DbGoods
from db.DbCategory import DbCategory
from db.DbBrand import DbBrand


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
                realContent.append('please check it.')
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
                realContent.append('please check it.')
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
                                  'brand_name': data.brand_name,
                                  'attr_market_year': data.attr_market_year}
                        realContent.append(string)
            elif isinstance(contentData, basestring):
                realContent = contentData
            else:
                realContent.append('please check it.')
            return {'code': obj.code, 'desc': obj.desc,
                    'result': realContent}
            # if isinstance(contentData, list):
            #     print contentData[0].author
            # else:
            #     print type(contentData)
        else:
            return json.JSONEncoder.default(self, obj)

"""
将HostGoods 转成 Json 字符串
"""
class HostGoodsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseResponse):
            contentData = obj.data
            # print type(contentData)
            realContent = []
            if isinstance(contentData, list):
                realContent.append('host goods not support return list')
            elif isinstance(contentData, NetHostGoods):
                category = contentData.dbCategory
                goodsList = contentData.dbGoodsList
                brandList = contentData.dbBrandList
                if isinstance(category, DbCategory):
                    cate_str = {'code': category.cate_code, 'name': category.cate_name, 'logo': category.cate_logo,
                                'id': category.cate_id}
                    realContent.append({'category': cate_str})
                goods_content = []
                if isinstance(goodsList, list):
                    for goods in goodsList:
                        if isinstance(goods, DbGoods):
                            brandName = ''
                            brandId = ''
                            if brandList and isinstance(brandList, list):
                                for brand in brandList:
                                    if isinstance(brand, DbBrand) and brand.brand_id == goods.brand_id:
                                        brandName = brand.brand_name
                                        brandId = brand.brand_id
                            goods_str = {'marketPrice': goods.market_price, 'saleCount': goods.sale_count,
                                         'businessName': brandName, 'businessId': brandId, 'thumLogo': goods.thum_logo,
                                         'title': goods.goods_name, 'price': goods.current_price, 'name': goods.goods_name,
                                         'stockNum': goods.stock_num, 'logo': goods.goods_logo, 'id': goods.goods_id}
                            goods_content.append(goods_str)
                realContent.append({'list': goods_content})
            elif isinstance(contentData, basestring):
                realContent = contentData
            else:
                realContent.append('please check it.')
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