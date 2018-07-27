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

    # =========================== 转换开始 ===================================== #

    # 将数据库查询的结果，对应设置给adverts 实体bean，并将adverts list 集合返回出去
    def convertDbRow2Adverts(self, dbAdvertsAllRowsResult):
        if not dbAdvertsAllRowsResult:
            return None
        advertsList = []
        for row in dbAdvertsAllRowsResult:
            adverts = DbAdverts()
            row_id = row[0]
            adverts.advert_id = row[1]
            adverts.cate_id = row[2]
            adverts.title = row[3]
            adverts.pic_url = row[4]
            adverts.sort = row[5]
            adverts.create_time = row[6]
            advertsList.append(adverts)
        return advertsList

    # 将数据库广告信息，转换为网络api 返回广告集合
    def convert2NetAdvertsList(self, dbAdvertsList, dbCateList):
        if not dbAdvertsList:
            return None
        if not dbCateList:
            return dbAdvertsList
        netAdvertsList = []
        for dbAdvert in dbAdvertsList:
            netAdverts = NetAdverts()
            netAdverts.id = dbAdvert.advert_id
            netAdverts.title = dbAdvert.title
            netAdverts.sort = dbAdvert.sort
            netAdverts.picUrl = dbAdvert.pic_url
            netAdverts.createTime = dbAdvert.create_time
            for dbCate in dbCateList:
                if dbCate.cate_id == dbAdvert.cate_id:
                    netAdverts.advertUrl = adverts_url_prefix + dbCate.cate_code
            netAdvertsList.append(netAdverts)
        return netAdvertsList

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