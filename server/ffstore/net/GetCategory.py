#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   get category 获取分类接口，返回网络数据

"""

from ffstore.db.CategoryDao import CategoryDao
from ffstore.db.AttributeDao import AttributeDao
from ffstore.db.DbCategory import DbCategory
from ffstore.db.DbAttribute import DbAttribute
from ffstore.net.NetCategory import NetCategory
from ffstore.net.NetDiscover import NetDiscover
from ffstore.constant import CategoryShowType

class GetCategory:

    def __init__(self):
        self.cateDao = CategoryDao()
        self.attrDao = AttributeDao()
        pass

    """
    从数据库获取商品分类
    """
    def getCategoryFromDb(self):
        print '--- getCategoryFromDb start ---'
        results = self.cateDao.queryAllCateFromDb()
        print results
        if results is None:
            return None
        categoryList = []
        for row in results:
            category = DbCategory()
            row_id = row[0]
            cate_id = row[1]
            cate_code = row[2]
            parent_code = row[3]
            cate_logo = row[4]
            cate_name = row[5]
            cate_show_type = row[6]
            category.cate_id = cate_id
            category.cate_code = cate_code
            category.parent_code = parent_code
            category.cate_logo = cate_logo
            category.cate_name = cate_name
            category.cate_show_type = cate_show_type
            categoryList.append(category)
            print "getCategoryFromDb row_id = %s, cate_id = %s, cate_code = %s, parent_code = %s cate_logo = %s, cate_name = %s" \
                  % (row_id, cate_id, cate_code, parent_code, cate_logo, cate_name)
        return categoryList

    """
    保存单个商品分类进数据库
    """
    def saveCategoryToDb(self, category=None):
        print '--- saveCategoryToDb start ---'
        if category is None or len(category) == 0:
            print "category is None could not save to db."
            return False
        else:
            return self.cateDao.saveOrUpdateToDb(category)


    """
    获取数据库所有的分类, 包括二级分类
    """
    def doGetCategory(self):
        dbCateList = self.getCategoryFromDb()
        if dbCateList:
            return self.convertCateDb2Net(dbCateList)
        else:
            return None

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
    def covertHomeDiscover2Net(self, dbCateList, dbAttrList):
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
                    netDiscover.attr_brand_name = dbAttr.attr_brand_name
                    netDiscover.attr_market_year = dbAttr.attr_market_year
                    break
            netDiscoverList.append(netDiscover)
        return netDiscoverList

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
            dbCate = DbCategory()
            row_id = row[0]
            cate_id = row[1]
            cate_code = row[2]
            parent_code = row[3]
            cate_logo = row[4]
            cate_name = row[5]
            cate_show_type = row[6]
            dbCate.cate_id = cate_id
            dbCate.cate_code = cate_code
            dbCate.parent_code = parent_code
            dbCate.cate_logo = cate_logo
            dbCate.cate_name = cate_name
            dbCate.cate_show_type = cate_show_type
            dbCateList.append(dbCate)
            if cate_id not in dbCateIds:
                dbCateIds.append(cate_id)
        # query cate attributes
        attrResult = self.attrDao.queryCateAttrs(dbCateIds)
        if not attrResult:
            return None
        dbAttrList = []
        for row in attrResult:
            dbAttr = DbAttribute()
            row_id = row[0]
            cate_id = row[1]
            goods_id = row[2]
            attr_market_year = row[3]
            attr_size = row[4]
            attr_color = row[5]
            dbAttr.cate_id = cate_id
            dbAttr.goods_id = goods_id
            dbAttr.attr_market_year = attr_market_year
            dbAttr.attr_size = attr_size
            dbAttr.attr_color = attr_color
            dbAttrList.append(dbAttr)
        # category not have brand_name
        return self.covertHomeDiscover2Net(dbCateList, dbAttrList)

    """
    获取首页展示的分类总数量
    """
    def getHomeDiscoverCount(self):
        homeDiscoverCount = self.cateDao.queryCateCountByShowType(CategoryShowType.TYPE_SHOW_HOME)
        return homeDiscoverCount

if __name__ == '__main__':
    getCate = GetCategory()
    getCate.doGetCategory()
    # categoryNetList = getCategoryFromNet()
    # saveCategoryToDb(categoryNetList)