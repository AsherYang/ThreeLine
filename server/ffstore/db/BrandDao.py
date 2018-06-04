#! /usr/bin/python
# -*- coding:utf-8 -*-


"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/5/22
Desc  : 操作厂家(品牌)数据表
"""
from ffstore.util import DbUtil


class BrandDao:
    def __init__(self):
        pass

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
