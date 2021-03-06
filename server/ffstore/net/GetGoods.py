#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/28
Desc:   获取商品接口. 返回网络数据
"""
import sys
sys.path.append('../')

from constant import GoodsSort
from db.CategoryDao import CategoryDao
from db.GoodsDao import GoodsDao
from db.BrandDao import BrandDao
from db.AttributeDao import AttributeDao
from db.GoodsPhotoDao import GoodsPhotoDao
from db.DbCategory import DbCategory
from db.DbGoods import DbGoods
from db.DbBrand import DbBrand
from db.DbAttribute import DbAttribute
from db.DbGoodsPhoto import DbGoodsPhoto
from net.NetHostGoods import NetHostGoods
from net.NetGoodsDetail import NetGoodsDetail
from util.LogUtil import LogUtil


class GetGoods:
    def __init__(self):
        self.cateDao = CategoryDao()
        self.goodsDao = GoodsDao()
        self.brandDao = BrandDao()
        self.attrDao = AttributeDao()
        self.photoDao = GoodsPhotoDao()
        self.logging = LogUtil().getLogging()

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
        if not goods:
            return None
        attrResult = self.attrDao.queryAttrListByGoodsId(goods_id)
        attrList = self.convertDbRow2AttrList(attrResult)
        brandResult = self.brandDao.queryBrandById(goods.brand_id)
        brand = self.convertDbRow2Brand(brandResult)
        photoResult = self.photoDao.queryPhotoListByGoodsId(goods_id)
        photoList = self.convertDbRow2PhotoList(photoResult)
        return self.convert2NetGoodsDetail(goods, attrList, brand, photoList)

    # 根据goodsIdList获取商品集合
    def getDbGoodsByIdList(self, goodsIdList):
        if not goodsIdList:
            return None
        goodsResult = self.goodsDao.queryGoodsListByGoodsIdList(goodsIdList)
        return self.convertDbRow2GoodsList(goodsResult)

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
        netHostGoods.dbCategory = category
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
    def getGoodsCountByCate(self, cate_code, goods_size):
        cateId = self.getCateIdByCateCode(cate_code)
        if not cateId:
            return None
        return self.goodsDao.queryGoodsCountByCateId(cateId, goods_size)

    # 获取分类进入二级分类页的商品, 根据条件搜索获取商品
    # goods_size: 尺码，对应接口skuval, 使用GoodsAttr常量类
    def getSearchGoodsList(self, searchKeywords, cate_code, goods_size, page_num=1, page_size=10, sort=GoodsSort.SORT_COMMON):
        category = self.getCateByCateCode(cate_code)
        if not category:
            return None
        goodsResult = self.goodsDao.queryGoodsByKeywords(searchKeywords, category.cate_id, goods_size,
                                                         page_num, page_size, sort)
        goodsList = self.convertDbRow2GoodsList(goodsResult)
        if not goodsList:
            return None
        netSearchGoods = NetHostGoods()
        netSearchGoods.dbCategory = category
        brandIdList = []
        for goods in goodsList:
            netSearchGoods.appendGoods(goods)
            brandIdList.append(goods.brand_id)
        brandResult = self.brandDao.queryBrandByIds(brandIdList)
        brandList = self.convertDbRow2BrandList(brandResult)
        if not brandList:
            return netSearchGoods
        for brand in brandList:
            netSearchGoods.appendBrand(brand)
        return netSearchGoods

    # 返回对应keyworld 模糊匹配的商品总数
    def getGoodsCountByKeywords(self, searchKeywords, cate_code, goods_size):
        cateId = self.getCateIdByCateCode(cate_code)
        return self.goodsDao.queryGoodsCountByKeywords(searchKeywords, cateId, goods_size)

    # 保存商品信息进数据库
    def saveOrUpdateToDb(self, goods):
        return self.goodsDao.saveOrUpdateToDb(goods=goods)

    # 更新商品信息
    def updateToDb(self, goods):
        return self.goodsDao.updateToDb(goods=goods)

    # 删除分类，以及分类下的所有商品
    def deleteCateAndGoods(self, cate_id):
        if not cate_id:
            return False
        deleteResult = self.cateDao.deleteByCateId(cate_id)
        if deleteResult:
            return self.goodsDao.deleteByCateId(cate_id)
        return False

    # 删除单个商品
    def deleteByGoodsId(self, goods_id):
        if not goods_id:
            return False
        return self.goodsDao.deleteByGoodsId(goods_id)

    # =========================== 转换开始 ===================================== #

    # 将数据库查询的结果，对应设置给goods 实体bean，并将单个 goods 返回出去
    def convertDbRow2Goods(self, dbGoodsRowResult):
        if not dbGoodsRowResult:
            return None
        dbGoods = DbGoods()
        dbSingleRow = dbGoodsRowResult[0]
        dbGoods.goods_id = dbSingleRow["goods_id"]
        dbGoods.cate_id = dbSingleRow["cate_id"]
        dbGoods.brand_id = dbSingleRow["brand_id"]
        dbGoods.goods_name = dbSingleRow["goods_name"]
        dbGoods.market_price = dbSingleRow["market_price"]
        dbGoods.current_price = dbSingleRow["current_price"]
        dbGoods.sale_count = dbSingleRow["sale_count"]
        dbGoods.stock_num = dbSingleRow["stock_num"]
        dbGoods.status = dbSingleRow["status"]
        dbGoods.goods_code = dbSingleRow["goods_code"]
        dbGoods.goods_logo = dbSingleRow["goods_logo"]
        dbGoods.thum_logo = dbSingleRow["thum_logo"]
        dbGoods.keywords = dbSingleRow["keywords"]
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
            dbGoods.status = row[9]
            dbGoods.goods_code = row[10]
            dbGoods.goods_logo = row[11]
            dbGoods.thum_logo = row[12]
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

    # 将数据库查询出来的结果，对应设置给brand实体bean, 并将单个 brand 返回出去
    def convertDbRow2Brand(self, dbBrandRowsResult):
        if not dbBrandRowsResult:
            return None
        dbBrand = DbBrand()
        row_id = dbBrandRowsResult[0]
        dbBrand.brand_id = dbBrandRowsResult[1]
        dbBrand.brand_name = dbBrandRowsResult[2]
        dbBrand.brand_logo = dbBrandRowsResult[3]
        return dbBrand

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

    # 将数据库查询出来的结果，对应设置给Attribute实体bean, 并作为集合返回出去
    def convertDbRow2AttrList(self, dbAttrAllRowsResult):
        if not dbAttrAllRowsResult:
            return None
        attrList = []
        # 元组的遍历 {@https://blog.csdn.net/u014267402/article/details/54601125}
        for i in range(len(dbAttrAllRowsResult)):
            dbAttr = DbAttribute()
            singleRow = dbAttrAllRowsResult[i]
            row_id = singleRow['_id']
            dbAttr.cate_id = singleRow['cate_id']
            dbAttr.goods_id = singleRow['goods_id']
            dbAttr.attr_market_year = singleRow['attr_market_year']
            dbAttr.attr_size = singleRow['attr_size']
            dbAttr.attr_color = singleRow['attr_color']
            attrList.append(dbAttr)
        return attrList

    # 将数据库查询出来的结果，对应设置给Attribute实体bean, 并作为集合返回出去
    def convertDbRow2PhotoList(self, dbPhotoAllRowsResult):
        if not dbPhotoAllRowsResult:
            return None
        photoList = []
        # 元组的遍历 {@https://blog.csdn.net/u014267402/article/details/54601125}
        for i in range(len(dbPhotoAllRowsResult)):
            dbGoodsPhoto = DbGoodsPhoto()
            singleRow = dbPhotoAllRowsResult[i]
            row_id = singleRow['_id']
            dbGoodsPhoto.goods_id = singleRow['goods_id']
            dbGoodsPhoto.photo = singleRow['photo']
            dbGoodsPhoto.thum_photo = singleRow['thum_photo']
            photoList.append(dbGoodsPhoto)
        return photoList

    # 将数据库商品信息，转换为网络api 返回商品数据
    def convert2NetGoodsDetail(self, goods, attrList, brand, photoList):
        if not goods:
            return None
        if isinstance(goods, DbGoods):
            netGoodsDetail = NetGoodsDetail()
            NetGoodsDetail.id = goods.goods_id
            netGoodsDetail.dbAttrList = attrList
            if brand:
                netGoodsDetail.businessId = brand.brand_id
                netGoodsDetail.businessName = brand.brand_name
            netGoodsDetail.code = goods.goods_code
            # netGoodsDetail.detailInfo =
            # netGoodsDetail.evaluateCount =
            netGoodsDetail.logo = goods.goods_logo
            netGoodsDetail.marketPrice = goods.market_price
            netGoodsDetail.name = goods.goods_name
            netGoodsDetail.dbPhotoList = photoList
            netGoodsDetail.price = goods.current_price
            netGoodsDetail.saleCount = goods.sale_count
            # netGoodsDetail.shareAmount
            # netGoodsDetail.shareTimes
            # netGoodsDetail.shareTips
            netGoodsDetail.status = goods.status
            netGoodsDetail.stockNum = goods.stock_num
            netGoodsDetail.thumLogo = goods.thum_logo
            return netGoodsDetail
        else:
            return None

    # =========================== 转换结束 ===================================== #
