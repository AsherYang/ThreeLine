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
    def queryCateAttrs(self, brand_id):
        query = 'SELECT * FROM ffstore_brand WHERE brand_id = "%s" ' % brand_id
        return DbUtil.query(query)
