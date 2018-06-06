#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/28
Desc:   获取商品接口. 返回网络数据
"""
from ffstore.constant import GoodsSort
from ffstore.db.CategoryDao import CategoryDao
from ffstore.db.DbCategory import DbCategory
from ffstore.db.DbGoods import DbGoods
from ffstore.db.DbBrand import DbBrand
from ffstore.db.GoodsDao import GoodsDao
from ffstore.db.BrandDao import BrandDao
from ffstore.net.NetHostGoods import NetHostGoods

class GetGoods:
    def __init__(self):
        self.cateDao = CategoryDao()
        self.goodsDao = GoodsDao()
        self.brandDao = BrandDao()
        pass

    # 根据cate_code 获取cate_id, cate_code 是唯一值属性
    def getCateIdByCateCode(self, cate_code):
        cateResult = self.cateDao.queryCateByCode(cate_code)
        if cateResult:
            for row in cateResult:
                return row[1]
        return None

    # 根据cate_code 获取单个category, cate_code 是唯一值属性
    def getCateByCateCode(self, cate_code):
        cateResult = self.cateDao.queryCateByCode(cate_code)
        category = self.convertDbRow2CateList(cateResult)
        if category and len(category) == 1:
            return category[0]
        return None

    # 根据cate_code 获取该category 分类下的所有商品
    def getGoodsByCateCode(self, cate_code):
        cateId = self.getCateIdByCateCode(cate_code)
        if not cateId:
            return None
        return self.getGoodsByCateId(cateId)

    # 根据cate_id 获取该category 分类下的所有商品
    def getGoodsByCateId(self, cate_id):
        if not cate_id:
            return None
        goodsResult = self.goodsDao.queryGoodsByCateId(cate_id)
        goodsList = self.convertDbRow2GoodsList(goodsResult)
        # todo
        # return convert2net

    # 根据商品ID 获取商品详细信息
    def getGoodsById(self, goods_id):
        if not goods_id:
            return None
        goodsResult = self.goodsDao.queryGoodsByGoodsId(goods_id)
        goods = self.convertDbRow2Goods(goodsResult)
        # todo
        # return convert2Net

    # 获取点击首页分类进入分类页的商品, 根据条件获取商品
    # goods_size: 尺码，对应接口skuval, 使用GoodsAttr常量类
    def getHostGoods(self, cate_code, goods_size, page_num=1, page_size=10, sort=GoodsSort.SORT_COMMON):
        category = self.getCateByCateCode(cate_code)
        if not category:
            return None
        goodsResult = self.goodsDao.querySortGoodsByCateId(category.cate_id, goods_size, page_num, page_size, sort)
        goodsList = self.convertDbRow2GoodsList(goodsResult)
        if not goodsList:
            return None
        netHostGoods = NetHostGoods()
        netHostGoods.category = category
        brandIdList = []
        for goods in goodsList:
            netHostGoods.appendGoods(goods)
            brandIdList.append(goods.brand_id)
        brandResult = self.brandDao.queryBrandByIds(brandIdList)
        brandList = self.convertDbRow2BrandList(brandResult)
        if not brandList:
            return netHostGoods
        for brand in brandList:
            netHostGoods.appendBrand(brand)
        return netHostGoods

    # 返回对应category 分类下商品总数
    def getGoodsCountByCate(self, cate_code):
        cateId = self.getCateIdByCateCode(cate_code)
        if not cateId:
            return None
        return self.goodsDao.queryGoodsCountByCateId(cateId)

    # 将数据库查询的结果，对应设置给goods 实体bean，并将goods 返回出去
    def convertDbRow2Goods(self, dbGoodsRowResult):
        if not dbGoodsRowResult:
            return None
        dbGoods = DbGoods()
        dbGoods.goods_id = dbGoodsRowResult[1]
        dbGoods.cate_id = dbGoodsRowResult[2]
        dbGoods.brand_id = dbGoodsRowResult[3]
        dbGoods.goods_name = dbGoodsRowResult[4]
        dbGoods.market_price = dbGoodsRowResult[5]
        dbGoods.current_price = dbGoodsRowResult[6]
        dbGoods.sale_count = dbGoodsRowResult[7]
        dbGoods.stock_num = dbGoodsRowResult[8]
        dbGoods.goods_code = dbGoodsRowResult[9]
        dbGoods.goods_logo = dbGoodsRowResult[10]
        dbGoods.thum_logo = dbGoodsRowResult[11]
        return dbGoods

    # 将数据库查询出来的结果，对应设置给goods实体bean，并作为集合返回出去
    def convertDbRow2GoodsList(self, dbGoodsAllRowsResult):
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
            dbGoods.stock_num = row[8]
            dbGoods.goods_code = row[9]
            dbGoods.goods_logo = row[10]
            dbGoods.thum_logo = row[11]
            goodsList.append(dbGoods)
        return goodsList

    # 将数据库查询出来的结果，对应设置给category实体bean, 并作为集合返回出去
    def convertDbRow2CateList(self, dbCateAllRowsResult):
        if not dbCateAllRowsResult:
            return None
        cateList = []
        for row in dbCateAllRowsResult:
            dbCate = DbCategory()
            row_id = row[0]
            dbCate.cate_id = row[1]
            dbCate.cate_code = row[2]
            dbCate.parent_code = row[3]
            dbCate.cate_logo = row[4]
            dbCate.cate_name = row[5]
            dbCate.cate_show_type = row[6]
            cateList.append(dbCate)
        return cateList

    # 将数据库查询出来的结果，对应设置给brand实体bean, 并作为集合返回出去
    def convertDbRow2BrandList(self, dbBrandAllRowsResult):
        if not dbBrandAllRowsResult:
            return None
        brandList = []
        for row in dbBrandAllRowsResult:
            dbBrand = DbBrand()
            row_id = row[0]
            dbBrand.brand_id = row[1]
            dbBrand.brand_name = row[2]
            dbBrand.brand_logo = row[3]
            brandList.append(dbBrand)
        return brandList

    # 删除分类，以及分类下的所有商品
    def deleteCateAndGoods(self, cate_id):
        if not cate_id:
            return False
        deleteResult = self.cateDao.deleteByCateId(cate_id)
        if deleteResult:
            return self.goodsDao.deleteByCateId(cate_id)
        return False

