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
from ffstore.constant import GoodsSort
from ffstore.constant import GoodsStatus


class GoodsDao:
    def __init__(self):
        pass

    def saveToDb(self, goods):
        if isinstance(goods, DbGoods):
            insert = 'insert into ffstore_goods (goods_id, cate_id, brand_id, goods_name, market_price, ' \
                     'current_price, sale_count, stock_num, status, goods_code, goods_logo, thum_logo) ' \
                     'values("%s", "%s", "%s", "%s", "%d", "%d", "%d", "%s" "%s", "%s", "%s")' \
                     % (goods.goods_id, goods.cate_id, goods.brand_id, goods.goods_name, goods.market_price,
                        goods.current_price, goods.sale_count, goods.stock_num, goods.status, goods.goods_code,
                        goods.goods_logo, goods.thum_logo)
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
                     'sale_count = "%s", stock_num = "%s", status = "%s", goods_code = "%s", goods_logo = "%s", ' \
                     'thum_logo = "%s" where goods_id = "%s"' \
                     % (goods.goods_name, goods.market_price, goods.current_price, goods.sale_count, goods.stock_num,
                        goods.status, goods.goods_code, goods.goods_logo, goods.thum_logo, goods.goods_id)
            print 'update goods to db'
            return DbUtil.update(update)
        return False

    # 更新商品状态{@see GoodsStatus}
    def updateSaleCount(self, goods_id, goods_status):
        if not goods_id:
            return False
        if goods_status != GoodsStatus.STATUS_ON_SALE or goods_status != GoodsStatus.STATUS_SALE_OUT:
            return False
        update = 'update ffstore_goods set status = "%s" where goods_id = "%s"' % (goods_status, goods_id)
        return DbUtil.update(update)

    # 更新商品卖出件数
    def updateSaleCount(self, goods_id, sale_count):
        if not goods_id:
            return False
        saleCount = 0 if sale_count < 0 else sale_count
        update = 'update ffstore_goods set sale_count = "%s" where goods_id = "%s"' % (saleCount, goods_id)
        return DbUtil.update(update)

    # 更新商品库存
    def updateStockNum(self, goods_id, stock_num):
        if not goods_id:
            return False
        stock_num = 0 if stock_num < 0 else stock_num
        update = 'update ffstore_goods set stock_num = "%s" where goods_id = "%s"' % (stock_num, goods_id)
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

    # 根据cate_id,分页查询单个分类下的商品，并按照给定sort进行排序
    # sort 排序于limit结合使用，可能会造成的问题及解决方法:
    # https://blog.csdn.net/qiubabin/article/details/70135556
    def querySortGoodsByCateId(self, cate_id, goods_size, page_num=1, page_size=10, sort=GoodsSort.SORT_COMMON):
        if not cate_id:
            return None
        start = (page_num - 1) * page_size
        if sort == GoodsSort.SORT_PRICE_DOWN:
            sort_str = 'current_price desc'
        elif sort == GoodsSort.SORT_PRICE_UP:
            sort_str = 'current_price asc'
        elif sort == GoodsSort.SORT_SALE_COUNT:
            sort_str = 'sale_count desc'
        else:
            sort_str = '_id desc'
        if not goods_size:
            query = 'select * from ffstore_goods where cate_id = "%s" order by _id, ' + sort_str + ' limit %s, %s;' \
                % (cate_id, start, page_size)
        else:
            # join ffstore_attr table
            query = 'select * from ffstore_goods left join ffstore_attr on ffstore_goods.goods_id = ' \
                    'ffstore_attr.goods_id where ffstore_goods.cate_id = "%s" and ' \
                    'ffstore_attr.attr_size = "%s" order by _id, ' + sort_str + ' limit %s, %s;' \
                % (cate_id, goods_size, start, page_size)
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

    # 删除商品
    def deleteGoods(self, goods):
        if isinstance(goods, DbGoods):
            delete = 'delete from ffstore_goods where goods_id = "%s" ' % goods.goods_id
            print 'delete goods:%s from db.' % goods
            return DbUtil.delete(delete)
        return False

    def deleteByGoodsId(self, goods_id):
        delete = 'delete from ffstore_goods where goods_id = "%s" ' % goods_id
        print 'delete goods by goods_id:%s from db.' % goods_id
        return DbUtil.delete(delete)

    # 删除该category目录下所有的商品
    def deleteByCateId(self, cate_id):
        delete = 'delete from ffstore_goods where cate_id = "%s" ' % cate_id
        print 'delete goods by cate_id:%s from db.' % cate_id
        return DbUtil.delete(delete)

