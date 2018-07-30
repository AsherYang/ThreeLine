#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 获取厂商信息，返回网络数据
"""
from util.GenerateIDUtil import GenerateIDUtil
from util.LogUtil import LogUtil
from ffstore.db.BrandDao import BrandDao
from ffstore.db.DbBrand import DbBrand
from ffstore.net.NetBrand import NetBrand


class GetBrand:
    def __init__(self):
        self.brandDao = BrandDao()
        self.logging = LogUtil().getLogging()
        pass

    """
    添加厂家
    """
    def addBrand(self, netBrand):
        if not netBrand:
            return False
        dbBrand = self.convert2DbBrand(netBrand)
        self.brandDao.saveToDb(dbBrand)

    """
    删除一家厂家
    """
    def deleteBrandById(self, brand_id):
        return self.brandDao.deleteBrandById(brand_id)

    """
    根据brand_id 查询一家厂商
    """
    def queryBrandById(self, brand_id):
        return self.brandDao.queryBrandById(brand_id)

    """
    根据brand_id 更新
    """
    def updateBrand(self, dbBrand):
        return self.brandDao.updateToDb(dbBrand=dbBrand)

    # =========================== 转换开始 ===================================== #

    # 将网络数据转换为数据库数据
    def convert2DbBrand(self, netBrand):
        if not netBrand:
            return None
        if isinstance(netBrand, NetBrand):
            dbBrand = DbBrand()
            if netBrand.brand_id:
                dbBrand.brand_id = netBrand.brand_id
            else:
                genIdUtil = GenerateIDUtil()
                dbBrand.brand_id = str(genIdUtil.getUID())
            dbBrand.brand_name = netBrand.brand_name
            dbBrand.brand_logo = netBrand.brand_logo
            return dbBrand
        return None

    # =========================== 转换结束 ===================================== #