#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 操作商品属性(ffstore_attr),返回网络数据
"""
from util.LogUtil import LogUtil
from ffstore.db.DbAttribute import DbAttribute
from ffstore.db.AttributeDao import AttributeDao


class GetGoodsAttr:
    def __init__(self):
        self.logging = LogUtil().getLogging()
        self.attrDao = AttributeDao()
        pass

    """
    添加商品属性
    """
    def addGoodsAttr(self, goodsAttr):
        if not goodsAttr:
            return False
        if isinstance(goodsAttr, DbAttribute):
            return self.attrDao.saveToDb(dbGoodsAttr=goodsAttr)
        return False

    """
    根据goods_id 更新
    """
    def updateGoodsAttr(self, goodsAttr):
        return self.attrDao.updateAttrByGoodsId(dbGoodsAttr=goodsAttr)

    # =========================== 转换开始 ===================================== #

    # =========================== 转换结束 ===================================== #