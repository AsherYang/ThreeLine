#! /usr/bin/python
# -*- coding:utf-8 -*-


"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/5/22
Desc  : 操作商品图片数据表
"""
from ffstore.util import DbUtil


class GoodsPhotoDao:
    def __init__(self):
        pass

    # 查询单个商品图片集合
    def queryPhotoListByGoodsId(self, goods_id):
        if not goods_id:
            return None
        query = 'SELECT * FROM ffstore_photo WHERE goods_id = "%s"' % goods_id
        return DbUtil.query(query)
