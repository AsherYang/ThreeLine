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
import time
from db.Category import Category
from db.Goods import Goods

"""
将JSON 数据转换为category
"""
class CategoryDecode(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        dic = super(CategoryDecode, self).decode(s)
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

"""
将JSON 数据转换为 goods
"""
class GoodsDecode(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        dic = super(GoodsDecode, self).decode(s)
        print dic
        goodList = []
        currentTime = int(time.time())
        for goodTmp in dic['result']['items']:
            # 每件商品可能分配放在不同的分类下，cate_id 不一样，这里我们将每个cate_id 下的商品单独出来做不同的商品
            # 故例如，如果1个商品在2个不同的分裂下，会当做2件不同的商品
            cates = goodTmp['cates']
            for cate in cates:
                goods = Goods()
                # cate_id 在 cates 集合下
                goods.cate_id = cate['cate_id']
                goods.cate_name = cate['cate_name']
                goods.itemid = goodTmp['itemid']
                goods.item_desc = goodTmp['item_desc']
                goods.item_name = goodTmp['item_name']
                # 只取一张图
                goods.imgs = goodTmp['imgs'][0]
                goods.price = goodTmp['price']
                goods.update_time = currentTime
                goodList.append(goods)
        return goodList