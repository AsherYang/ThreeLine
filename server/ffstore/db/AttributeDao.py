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
from db.DbAttribute import DbAttribute


class AttributeDao:
    def __init__(self):
        pass

    # 插入商品属性
    def saveToDb(self, dbGoodsAttr):
        if isinstance(dbGoodsAttr, DbAttribute):
            insert = 'insert into ffstore_attr (cate_id, goods_id, attr_market_year, attr_size, attr_color) ' \
                     'values("%s", "%s", "%s", "%s", "%s")' \
                     % (dbGoodsAttr.cate_id, dbGoodsAttr.goods_id, dbGoodsAttr.attr_market_year,
                        dbGoodsAttr.attr_size, dbGoodsAttr.attr_color)
            return DbUtil.insert(insert)
        return False

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

    # 删除商品属性
    def deleteAttrByGoodsId(self, goodsId):
        if not goodsId:
            return False
        delete = 'delete from ffstore_attr where goods_id = "%s" ' % goodsId
        return DbUtil.delete(delete)

    # 更新商品属性
    def updateAttrByGoodsId(self, dbGoodsAttr):
        if isinstance(dbGoodsAttr, DbAttribute):
            if not dbGoodsAttr.goods_id:
                return False
            update = 'update ffstore_attr set cate_id = "%s", attr_market_year = "%s", attr_size = "%s", ' \
                     'attr_color = "%s" where goods_id = "%s"' \
                     % (dbGoodsAttr.cate_id, dbGoodsAttr.attr_market_year, dbGoodsAttr.attr_size,
                        dbGoodsAttr.attr_color, dbGoodsAttr.goods_id)
            return DbUtil.update(update)
        return False
