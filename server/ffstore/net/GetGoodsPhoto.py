#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 操作商品图片,返回网络数据
"""
from util.LogUtil import LogUtil
from net.NetGoodPhoto import NetGoodPhoto
from db.DbGoodsPhoto import DbGoodsPhoto
from db.GoodsPhotoDao import GoodsPhotoDao


class GetGoodsPhoto:
    def __init__(self):
        self.logging = LogUtil().getLogging()
        self.photoDao = GoodsPhotoDao()
        pass

    """
    添加商品图片
    """
    def addGoodsPhoto(self, goodsPhoto):
        if not goodsPhoto:
            return False
        if isinstance(goodsPhoto, NetGoodPhoto):
            dbGoodsPhoto = self.convert2DbPhoto(goodsPhoto)
        else:
            dbGoodsPhoto = goodsPhoto
        return self.photoDao.saveToDb(dbGoodsPhoto)

    """
    删除商品图片
    """
    def deleteGoodsPhotoById(self, goods_id):
        return self.photoDao.deletePhotoByGoodsId(goods_id)

    """
    根据goods_id 查询一件商品的图片集合
    """
    def queryPhotoByGoodId(self, goods_id):
        return self.photoDao.queryPhotoListByGoodsId(goods_id)

    """
    根据goods_id 更新
    """
    def updatePhoto(self, dbGoodsPhoto):
        return self.photoDao.updatePhoto(dbGoodsPhoto)

    # =========================== 转换开始 ===================================== #

    # 将网络数据转换为数据库数据
    def convert2DbPhoto(self, netGoodsPhoto):
        if not netGoodsPhoto:
            return None
        if isinstance(netGoodsPhoto, NetGoodPhoto):
            dbGoodsPhoto = DbGoodsPhoto()
            dbGoodsPhoto.goods_id = netGoodsPhoto.goods_id
            dbGoodsPhoto.photo = netGoodsPhoto.photo
            dbGoodsPhoto.thum_photo = netGoodsPhoto.thum_photo
            return dbGoodsPhoto
        return None

    # =========================== 转换结束 ===================================== #