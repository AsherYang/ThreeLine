#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   get category 获取分类接口，返回网络数据

"""
import sys

sys.path.append('../')

from db.CategoryDao import CategoryDao
from db.AttributeDao import AttributeDao
from db.DbCategory import DbCategory
from db.DbAttribute import DbAttribute
from net.NetCategory import NetCategory
from net.NetDiscover import NetDiscover
from constant import CategoryShowType


class GetCategory:
    def __init__(self):
        self.cateDao = CategoryDao()
        self.attrDao = AttributeDao()

    """
    从数据库获取商品分类
    """
    def getCategoryListFromDb(self):
        print '--- getCategoryFromDb start ---'
        results = self.cateDao.queryAllCateFromDb()
        print results
        if results is None:
            return None
        categoryList = []
        for row in results:
            category = self.convertDbRow2Cate(row)
            if not category:
                continue
            categoryList.append(category)
        return categoryList

    """
    根据cate_code 从数据库中获取商品分类信息
    """
    def getCategoryFromDb(self, cate_code):
        result = self.cateDao.queryCateByCode(cateCode=cate_code)
        if not result:
            return None
        return self.convertDbRow2Cate(result)

    """
    保存单个商品分类进数据库
    """
    def saveCategoryToDb(self, category=None):
        print '--- saveCategoryToDb start ---'
        if category is None:
            print "category is None could not save to db."
            return False
        return self.cateDao.saveOrUpdateToDb(category)

    """
    更新单个商品分类信息
    """
    def updateCategoryToDb(self, category=None):
        if not category:
            return False
        return self.cateDao.updateToDb(cate=category)


    """
    获取数据库所有的分类, 包括二级分类
    """
    def doGetCategory(self):
        dbCateList = self.getCategoryListFromDb()
        if dbCateList:
            return self.convertCateDb2Net(dbCateList)
        else:
            return None

    """
    获取首页展示的分类列表，对应API：api/mall/discoverList
    """
    def getHomeDiscoverList(self, page_num=1, page_size=10):
        result = self.cateDao.queryCateListByShowType(CategoryShowType.TYPE_SHOW_HOME, page_num, page_size)
        if result is None:
            print 'there is no TYPE_SHOW_HOME category, please add it.'
            return None
        dbCateIds = []
        dbCateList = []
        for row in result:
            dbCate = self.convertDbRow2Cate(row)
            if not dbCate:
                continue
            dbCateList.append(dbCate)
            cate_id = dbCate.cate_id
            if cate_id not in dbCateIds:
                dbCateIds.append(cate_id)
        # query cate attributes
        attrResult = self.attrDao.queryCateAttrList(dbCateIds)
        if not attrResult:
            return None
        dbAttrList = []
        for row in attrResult:
            dbAttr = self.convertDbRow2Attr(row)
            if not dbAttr:
                continue
            dbAttrList.append(dbAttr)
        # category not have brand_name
        return self.convertHomeDiscover2Net(dbCateList, dbAttrList)

    """
    获取首页展示的分类总数量
    """
    def getHomeDiscoverCount(self):
        homeDiscoverCount = self.cateDao.queryCateCountByShowType(CategoryShowType.TYPE_SHOW_HOME)
        return homeDiscoverCount

    # =========================== 转换开始 ===================================== #

    """
    将数据库查询的结果，对应设置给dbCategory 实体bean，并将单个 cate 返回出去
    """
    def convertDbRow2Cate(self, dbCateRowResult):
        if not dbCateRowResult:
            return None
        category = DbCategory()
        row_id = dbCateRowResult[0]
        cate_id = dbCateRowResult[1]
        cate_code = dbCateRowResult[2]
        parent_code = dbCateRowResult[3]
        cate_logo = dbCateRowResult[4]
        cate_name = dbCateRowResult[5]
        cate_show_type = dbCateRowResult[6]
        category.cate_id = cate_id
        category.cate_code = cate_code
        category.parent_code = parent_code
        category.cate_logo = cate_logo
        category.cate_name = cate_name
        category.cate_show_type = cate_show_type
        return category

    """
    将数据库查询的结果，对应设置给DbAttributey 实体bean，并将单个 attr 返回出去
    """
    def convertDbRow2Attr(self, dbAttrRowResult):
        if not dbAttrRowResult:
            return None
        dbAttr = DbAttribute()
        row_id = dbAttrRowResult[0]
        cate_id = dbAttrRowResult[1]
        goods_id = dbAttrRowResult[2]
        attr_market_year = dbAttrRowResult[3]
        attr_size = dbAttrRowResult[4]
        attr_color = dbAttrRowResult[5]
        dbAttr.cate_id = cate_id
        dbAttr.goods_id = goods_id
        dbAttr.attr_market_year = attr_market_year
        dbAttr.attr_size = attr_size
        dbAttr.attr_color = attr_color
        return dbAttr

    """
    将商品分类数据库数据转换为网络数据，提供API数据
    """
    def convertCateDb2Net(self, dbCateList):
        if not dbCateList:
            return None
        categoryList = []
        for dbCate in dbCateList:
            netCate = NetCategory()
            netCate.id = dbCate.cate_id
            netCate.code = dbCate.cate_code
            netCate.parent_code = dbCate.parent_code
            netCate.name = dbCate.cate_name
            netCate.logo = dbCate.cate_logo
            categoryList.append(netCate)
        return categoryList

    """
    将商品分类数据库数据转换为用于首页展示的网络数据，提供API
    """
    def convertHomeDiscover2Net(self, dbCateList, dbAttrList):
        if not dbCateList or not dbAttrList:
            return None
        netDiscoverList = []
        for dbCate in dbCateList:
            netDiscover = NetDiscover()
            netDiscover.code = dbCate.cate_code
            netDiscover.logo = dbCate.cate_logo
            netDiscover.id = dbCate.cate_id
            for dbAttr in dbAttrList:
                if dbCate.cate_id == dbAttr.cate_id:
                    # 分类没有厂家名称
                    # netDiscover.brand_name = dbAttr.brand_name
                    netDiscover.attr_market_year = dbAttr.attr_market_year
                    break
            netDiscoverList.append(netDiscover)
        return netDiscoverList
    # =========================== 转换结束 ===================================== #


if __name__ == '__main__':
    getCate = GetCategory()
    getCate.doGetCategory()
    # categoryNetList = getCategoryFromNet()
    # saveCategoryToDb(categoryNetList)
