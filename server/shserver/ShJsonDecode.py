#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/8.
Desc:  JSON convert to Object
"""
import json
from json.decoder import WHITESPACE
from Category import Category
import time

"""
将JSON 数据转换为category
"""
class categoryDecode(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        dic = super(categoryDecode, self).decode(s)
        print dic
        categoryList = []
        currentTime = int(time.time())
        for categoryTmp in dic['result']:
            category = Category()
            category.cate_id = categoryTmp['cate_id']
            category.cate_name = categoryTmp['cate_name']
            category.parent_id = categoryTmp['parent_id']
            category.parent_cate_name = categoryTmp['parent_cate_name']
            category.sort_num = categoryTmp['sort_num']
            category.cate_item_num = categoryTmp['cate_item_num']
            category.description = categoryTmp['description']
            category.listUrl = categoryTmp['listUrl']
            category.shopName = categoryTmp['shopName']
            category.shopLogo = categoryTmp['shopLogo']
            category.update_time = currentTime
            categoryList.append(category)
        return categoryList
