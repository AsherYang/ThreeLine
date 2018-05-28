#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/28
Desc:   商品数据库操作类
"""

from ffstore.util import DbUtil
from DbGoods import DbGoods

class GoodsDao:

    def __init__(self):
        pass

    def saveToDb(self, goods):
        if isinstance(goods, DbGoods):
            insert = 'insert into ffstore_goods (goods_id, cate_id, brand_id, goods_name, market_price, ' \
                     'current_price, sale_count, goods_code, goods_logo, thum_logo) ' \
                     'values("%s", "%s", "%s", "%s", "%d", "%d", "%d", "%s", "%s", "%s")' \
                     % (goods.goods_id, goods.cate_id, goods.brand_id, goods.goods_name, goods.market_price,
                        goods.current_price, goods.sale_count, goods.goods_code, goods.goods_logo, goods.thum_logo)
            print 'insert goods to db.'
            return DbUtil.insert(insert)
        return False

