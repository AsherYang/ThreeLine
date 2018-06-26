#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 获取首页广告(banner)接口，返回网络数据
"""
from db.AdvertsDao import AdvertsDao
from db.DbAdverts import DbAdverts
from db.CategoryDao import CategoryDao
from net.NetAdverts import NetAdverts
from util.GenerateIDUtil import GenerateIDUtil


adverts_url_prefix = '/pages/home_detail?code='


class GetAdverts:
    def __init__(self):
        self.advertDao = AdvertsDao()
        self.cateDao = CategoryDao()
        pass

    """
    获取最近的广告
    用于在首页banner 展示
    last_count: 需要显示的最新条数
    """

    def getLastAdverts(self, last_count=5):
        advertsResult = self.advertDao.queryLastAdverts(last_count)
        if not advertsResult:
            return None
        dbAdvertsList = self.convertDbRow2Adverts(advertsResult)
        if not dbAdvertsList:
            return None
        cateIdList = []
        for adverts in dbAdvertsList:
            cateIdList.append(adverts.cate_id)
        dbCateList = self.cateDao.queryCateListByIdList(cateIdList)
        return self.convert2NetAdvertsList(dbAdvertsList, dbCateList)

    """
    添加广告, 一条广告一条广告的插入
    """
    def addAdverts(self, netAdverts, netCategory):
        if not netAdverts:
            return False
        dbAdverts = self.convert2DbAdverts(netAdverts, netCategory)
        if not dbAdverts:
            return False
        return self.advertDao.saveToDb(dbAdverts)

    """
    删除一条广告
    """
    def deleteAdvertsById(self, advert_id):
        return self.advertDao.deleteById(advert_id)

    """
    根据cate来删除广告，一般用于当该分类被删除时，对应的广告也被删除
    """
    def deleteAdvertsByCateId(self, cateId):
        return self.advertDao.deleteByCateId(cateId)

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
    def convert2DbAdverts(self, netAdverts, netCategory):
        if not netAdverts:
            return None
        if isinstance(netAdverts, NetAdverts):
            dbAdvert = DbAdverts()
            dbAdvert.sort = netAdverts.sort
            dbAdvert.title = netAdverts.title
            dbAdvert.create_time = netAdverts.createTime
            dbAdvert.pic_url = netAdverts.picUrl
            if netAdverts.id:
                dbAdvert.advert_id = netAdverts.id
            else:
                genIdUtil = GenerateIDUtil()
                dbAdvert.advert_id = genIdUtil.getUID()
            if netCategory:
                dbAdvert.cate_id = netCategory.id
            return dbAdvert
        return None

    # =========================== 转换结束 ===================================== #