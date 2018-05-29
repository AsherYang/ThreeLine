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

    # 此处会更新所有字段，需要注意，如果只想更新单个字段，请使用其他方法
    # 如果更新全部字段，请注意字段值的有效性，否则会更新掉原有的字段值
    def updateToDb(self, goods):
        if isinstance(goods, DbGoods):
            if not goods.goods_id:
                return False
            update = 'update ffstore_goods set goods_name = "%s", market_price = "%s", current_price = "%s", ' \
                     'sale_count = "%s", goods_code = "%s", goods_logo = "%s", thum_logo = "%s" where goods_id = "%s"' \
                     % (goods.goods_name, goods.market_price, goods.current_price, goods.sale_count, goods.goods_code,
                        goods.goods_logo, goods.thum_logo, goods.goods_id)
            print 'update goods to db'
            return DbUtil.update(update)
        return False

    # 更新商品卖出件数
    def updateSaleCount(self, goods_id, sale_count):
        if not goods_id:
            return False
        saleCount = 0 if sale_count < 0 else sale_count
        update = 'update ffstore_goods set sale_count = "%s" where goods_id = "%s"' % (saleCount, goods_id)
        return DbUtil.update(update)

    # 更新商品市场价，一般指原价
    def updateMarketPrice(self, goods_id, market_price):
        if not goods_id:
            return False
        marketPrice = 0 if market_price < 0 else market_price
        update = 'update ffstore_goods set market_price = "%s" where goods_id = "%s"' % (marketPrice, goods_id)
        return DbUtil.update(update)

    # 更新商品现价，也就是准备卖的价格
    def updateCurrentPrice(self, goods_id, current_price):
        if not goods_id:
            return False
        currentPrice = 0 if current_price < 0 else current_price
        update = 'update ffstore_goods set current_price = "%s" where goods_id = "%s"' % (currentPrice, goods_id)
        return DbUtil.update(update)

    # 查询所有商品
    def queryAllGoods(self):
        query = 'select * from ffstore_goods'
        return DbUtil.query(query)

    # 查询总商品数量
    def queryAllGoodsCount(self):
        query = 'select COUNT(*) from ffstore_goods'
        return DbUtil.query(query)

    # 根据cate_id 查询单个分类的所有商品
    def queryGoodsByCateId(self, cate_id):
        if not cate_id:
            return None
        query = 'select * from ffstore_goods where cate_id = "%s"' % cate_id
        return DbUtil.query(query)

    # 根据cate_id 查询单个分类的商品数量
    def queryGoodsCountByCateId(self, cate_id):
        if not cate_id:
            return None
        query = 'select COUNT(*) from ffstore_goods where cate_id = "%s"' % cate_id
        return DbUtil.query(query)

    # 查询单个商品
    def queryGoodsByGoodsId(self, goods_id):
        if not goods_id:
            return None
        query = 'select * from ffstore_goods where goods_id = "%s"' % goods_id
        return DbUtil.query(query)

