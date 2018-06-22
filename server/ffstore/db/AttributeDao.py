#! /usr/bin/python
# -*- coding:utf-8 -*-


"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/5/22
Desc  : 操作属性数据表
"""

import sys
sys.path.append('../')

from util import DbUtil


class AttributeDao:
    def __init__(self):
        pass

    # 根据给定的分类列表获取各个分类的属性描述
    # 返回包含查询分类的属性值集合(多个分类，每个分类可能有多条属性)
    def queryCateAttrList(self, cateIdList):
        if cateIdList is None:
            return None
        format_str = ','.join(['%s'] * len(cateIdList))
        query = 'SELECT * FROM ffstore_attr WHERE cate_id IN (%s)' % format_str, tuple(cateIdList)
        return DbUtil.query(query)

    # 查询单个商品属性
    def queryAttrListByGoodsId(self, goodsId):
        if not goodsId:
            return None
        query = 'SELECT * FROM ffstore_attr WHERE goods_id = "%s"' % goodsId
        return DbUtil.query(query)
