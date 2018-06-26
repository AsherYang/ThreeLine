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
from ffstore.db.CategoryDao import CategoryDao
from ffstore.net.NetAdverts import NetAdverts

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

    def getLastAdverts(self, last_count):
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

    """
    添加广告
    """
    def addAdverts(self):
        pass

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

    # =========================== 转换结束 ===================================== #