#! /usr/bin/python
# -*- coding:utf-8 -*-


"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/5/22
Desc  : 操作商品图片数据表
"""

import sys
sys.path.append('../')

from util import DbUtil
from db.DbGoodsPhoto import DbGoodsPhoto

class GoodsPhotoDao:
    def __init__(self):
        pass

    # 插入商品图片
    def saveToDb(self, dbGoodsPhoto):
        if isinstance(dbGoodsPhoto, DbGoodsPhoto):
            insert = 'insert into ffstore_photo (goods_id, photo, thum_photo) values("%s", "%s", "%s")' \
                     % (dbGoodsPhoto.goods_id, dbGoodsPhoto.photo, dbGoodsPhoto.thum_photo)
            return DbUtil.insert(insert)
        return False

    # 批量插入商品图片
    def saveListToDb(self, dbGoodsPhotoList):
        insert = 'insert into ffstore_photo (goods_id, photo, thum_photo) values '
        hasData = False
        if not dbGoodsPhotoList:
            return False
        for dbGoodsPhoto in dbGoodsPhotoList:
            if isinstance(dbGoodsPhoto, DbGoodsPhoto):
                insertTmp = '("%s", "%s", "%s"), ' % (dbGoodsPhoto.goods_id, dbGoodsPhoto.photo, dbGoodsPhoto.thum_photo)
                insert += insertTmp
                hasData = True
        if hasData:
            insert = insert.rstrip(', ')
            return DbUtil.insert(insert)
        else:
            return False


    # 查询单个商品图片集合
    def queryPhotoListByGoodsId(self, goods_id):
        if not goods_id:
            return None
        query = 'SELECT * FROM ffstore_photo WHERE goods_id = "%s"' % goods_id
        return DbUtil.query(query)

    # 删除商品图片
    def deletePhotoByGoodsId(self, goods_id):
        if not goods_id:
            return False
        delete = 'delete from ffstore_photo where goods_id = "%s" ' % goods_id
        print 'delete goods photo by goods_id:%s from db.' % goods_id
        return DbUtil.delete(delete)

    # 更新商品图片
    def updatePhoto(self, dbGoodsPhoto):
        if isinstance(dbGoodsPhoto, DbGoodsPhoto):
            if not dbGoodsPhoto.goods_id:
                return False
            update = 'update ffstore_photo set photo = "%s", thum_photo = "%s" where goods_id = "%s"' \
                     % (dbGoodsPhoto.photo, dbGoodsPhoto.thum_photo, dbGoodsPhoto.goods_id)
            print 'update goods photo to db'
            return DbUtil.update(update)
        return False