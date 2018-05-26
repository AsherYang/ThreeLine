#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   get category

"""

from ffstore.db.CategoryDao import CategoryDao
from ffstore.db.DbCategory import DbCategory
from ffstore.db.AttributeDao import AttributeDao
from ffstore.net.NetCategory import NetCategory
from ffstore.net.NetDiscover import NetDiscover
from ffstore.constant import CategoryShowType

class GetCategory:

    def __init__(self):
        pass

    """
    从数据库获取商品分类
    """
    def getCategoryFromDb(self):
        print '--- getCategoryFromDb start ---'
        results = CategoryDao.queryAllCateFromDb()
        print results
        if results is None:
            return None
        categoryList = []
        for row in results:
            category = DbCategory()
            row_id = row[0]
            cate_id = row[1]
            cate_code = row[2]
            cate_logo = row[3]
            cate_name = row[4]
            category.cate_id = cate_id
            category.cate_code = cate_code
            category.cate_logo = cate_logo
            category.cate_name = cate_name
            categoryList.append(category)
            print "row_id = %s, cate_id = %s, cate_code = %s, cate_logo = %s, cate_name = %s" \
                  % (row_id, cate_id, cate_code, cate_logo, cate_name)
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
            return CategoryDao.saveOrUpdateToDb(category)


    """
    category 更新策略：
    每天只更新一次
    返回值：当前有效的 category list
    """
    def doGetCategory(self):
        dbCateList = self.getCategoryFromDb()
        if dbCateList:
            return self.covertCateDb2Net(dbCateList)
        else:
            return None

    """
    将商品分类数据库数据转换为网络数据，提供API数据
    """
    def covertCateDb2Net(self, dbCateList):
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
        return netDiscover

    """
    获取首页展示的分类列表，对应API：api/mall/discoverList
    """
    def getHomeDiscoverList(self):
        dbCateList = CategoryDao.queryCateListByShowType(CategoryShowType.TYPE_SHOW_HOME)
        if dbCateList is None:
            print 'there is no TYPE_SHOW_HOME category, please add it.'
            return None
        dbCateIds = []
        for dbCate in dbCateList:
            if dbCate.cate_id not in dbCateIds:
                dbCateIds.append(dbCate.cate_id)
        # query cate attributes
        dbAttrList = AttributeDao.queryCateAttrs(dbCateIds)
        if not dbAttrList:
            return None
        return self.covertHomeDiscover2Net(dbCateList, dbAttrList)


if __name__ == '__main__':
    getCate = GetCategory()
    getCate.doGetCategory()
    # categoryNetList = getCategoryFromNet()
    # saveCategoryToDb(categoryNetList)