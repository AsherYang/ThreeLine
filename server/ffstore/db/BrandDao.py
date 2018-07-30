#! /usr/bin/python
# -*- coding:utf-8 -*-


"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/5/22
Desc  : 操作厂家(品牌)数据表
"""
import sys
sys.path.append('../')

from db.DbBrand import DbBrand
from util import DbUtil


class BrandDao:
    def __init__(self):
        pass

    def saveToDb(self, dbBrand):
        if isinstance(dbBrand, DbBrand):
            insert = 'insert into ffstore_brand (brand_id, brand_name, brand_logo) ' \
                     'values("%s", "%s", "%s") ' \
                     % (dbBrand.brand_id, dbBrand.brand_name, dbBrand.brand_logo)
            return DbUtil.insert(insert)
        return False

    def updateToDb(self, dbBrand):
        if isinstance(dbBrand, DbBrand):
            if not dbBrand.brand_id:
                return False
            else:
                update = 'update ffstore_brand set brand_name = "%s", brand_logo = "%s" where brand_id = "%s"; ' \
                         % (dbBrand.brand_name, dbBrand.brand_logo, dbBrand.brand_id)
                print 'update brand to db'
                return DbUtil.update(update)
        return False

    # 根据给定的厂家id 获取该厂家的信息
    def queryBrandById(self, brand_id):
        query = 'SELECT * FROM ffstore_brand WHERE brand_id = "%s" ' % brand_id
        return DbUtil.query(query)

    # 根据给定的厂家id列表获取各个厂家的属性描述
    # 返回包含查询厂家的属性值集合(多个厂家，每个厂家可能有多条属性)
    def queryBrandByIds(self, brandIdList):
        if brandIdList is None:
            return None
        format_str = ','.join(['%s'] * len(brandIdList))
        query = 'SELECT * FROM ffstore_brand WHERE brand_id IN (%s)' % format_str, tuple(brandIdList)
        return DbUtil.query(query)

    # 根据brand_id 删除厂家信息
    def deleteBrandById(self, brand_id):
        if brand_id is None:
            return False
        delete = 'delete from ffstore_brand where brand_id = "%s" ' % brand_id
        return DbUtil.delete(delete)
