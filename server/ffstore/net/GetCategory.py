#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   get category

"""

from ffstore.db.CategoryDao import CategoryDao
from ffstore.db.Category import Category


class GetCategory():

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
            category = Category()
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
            return False

    """
    将商品分类数据库数据转换为网络数据，提供API数据
    """
    def covertCateDb2Net(self, dbCateList):
        if not dbCateList:
            return False
        for dbCate in dbCateList:
            #TODO
            pass


if __name__ == '__main__':
    getCate = GetCategory()
    getCate.doGetCategory()
    # categoryNetList = getCategoryFromNet()
    # saveCategoryToDb(categoryNetList)