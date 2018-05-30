#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/28
Desc:   获取商品接口.
"""
from ffstore.db.CategoryDao import CategoryDao
from ffstore.db.GoodsDao import GoodsDao
from ffstore.db.DbGoods import DbGoods
from ffstore.constant import GoodsSort


class GetGoods:
    def __init__(self):
        pass

    def getCateIdByCateCode(self, cate_code):
        cateResult = CategoryDao.queryCateByCode(cate_code)
        if cateResult:
            for row in cateResult:
                return row[1]
        return None

    def getGoodsByCateCode(self, cate_code):
        cateId = self.getCateIdByCateCode(cate_code)
        if not cateId:
            return None
        goodsResult = GoodsDao.queryGoodsByCateId(cateId)
        goodsList = self.covertDbRow2List(goodsResult)
        # todo
        # return covert2Net


    # 获取点击首页分类进入分类页的商品, 根据条件获取商品
    # goods_size: 尺码，对应接口skuval, 使用GoodsAttr常量类
    def getHostGoods(self, cate_code, goods_size, page_num=1, page_size=10, sort=GoodsSort.SORT_COMMON):
        cateId = self.getCateIdByCateCode(cate_code)
        if not cateId:
            return None
        goodsResult = GoodsDao.querySortGoodsByCateId(cateId, goods_size, page_num, page_size, sort)
        goodsList = self.covertDbRow2List(goodsResult)
        # todo
        # return covert2Net

    # 返回对应category 分类下商品总数
    def getGoodsCountByCate(self, cate_code):
        cateId = self.getCateIdByCateCode(cate_code)
        if not cateId:
            return None
        return GoodsDao.queryGoodsCountByCateId(cateId)

    # 将数据库查询出来的结果，对应设置给实体bean，并作为集合返回出去
    def covertDbRow2List(self, dbGoodsAllRowsResult):
        if not dbGoodsAllRowsResult:
            return None
        goodsList = []
        for row in dbGoodsAllRowsResult:
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
        return goodsList
