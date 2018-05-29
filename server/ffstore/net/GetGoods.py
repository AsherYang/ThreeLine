#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/28
Desc:   获取商品接口.
"""
from ffstore.db.DbCategory import DbCategory
from ffstore.db.CategoryDao import CategoryDao
from ffstore.db.GoodsDao import GoodsDao
from ffstore.db.DbGoods import DbGoods

class GetGoods:
    def __init__(self):
        pass

    def getGoodsByCateCode(self, cateCode):
        cateResult = CategoryDao.queryCateByCode(cateCode)
        dbCate = DbCategory()
        if cateResult:
            for row in cateResult:
                dbCate.cate_id = row[1]
                break
        if not dbCate.cate_id:
            return None
        goodsResult = GoodsDao.queryGoodsByCateId(dbCate.cate_id)
        if not goodsResult:
            return None
        goodsList = []
        for row in goodsResult:
            dbGoods = DbGoods()
            row_id = row[0]
            dbGoods.goods_id = row[1]
            dbGoods.cate_id = row[2]
            dbGoods.brand_id = row[3]
            dbGoods.goods_name = row[4]
            dbGoods.market_price = row[5]
            dbGoods.current_price = row[6]
            dbGoods.sale_count = row[7]
            dbGoods.goods_code = row[8]
            dbGoods.goods_logo = row[9]
            dbGoods.thum_logo = row[10]
            goodsList.append(dbGoods)
        # TODO need to convert to network
        return goodsList