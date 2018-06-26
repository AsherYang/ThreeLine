#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 广告(banner)数据库操作
"""

from util import DbUtil

from DbAdverts import DbAdverts


class AdvertsDao:
    def __init__(self):
        pass

    def saveToDb(self, advert):
        if isinstance(advert, DbAdverts):
            insert = 'insert into ffstore_adverts (advert_id, cate_id, title, pic_url, sort, create_time)' \
                     ' values("%s", "%s", "%s", "%s", "%d", "%s")' \
                     % (advert.advert_id, advert.cate_id, advert.title, advert.pic_url, advert.sort, advert.create_time)
            print 'insert advert to db.'
            return DbUtil.insert(insert)
        return False

    def updateToDb(self, advert):
        if isinstance(advert, DbAdverts):
            if not advert.advert_id:
                return False
            else:
                update = 'update ffstore_adverts set cate_id = "%s", title = "%s", pic_url="%s", sort="%d",' \
                         ' create_time="%s" where advert_id = "%s" ' \
                         % (advert.cate_id, advert.title, advert.pic_url, advert.sort, advert.create_time,
                            advert.advert_id)
                print 'update adverts to db'
                return DbUtil.update(update)
        return False

    def updateSortToDb(self, advert):
        if isinstance(advert, DbAdverts):
            if not advert.sort:
                return False
            else:
                update = 'update ffstore_adverts set sort="%d" where advert_id = "%s" ' % (
                    advert.sort, advert.advert_id)
                return DbUtil.update(update)
        return False

    def deleteByCateId(self, cate_id):
        if not cate_id:
            return False
        delete = 'delete from ffstore_adverts where cate_id = "%s" ' % cate_id
        return DbUtil.delete(delete)

    def deleteById(self, advert_id):
        if not advert_id:
            return False
        delete = 'delete from ffstore_adverts where advert_id = "%s" ' % advert_id
        return DbUtil.delete(delete)

    # 查询所有广告
    def queryAllAdverts(self):
        query = 'select * from ffstore_adverts'
        return DbUtil.query(query)

    # 查询最新几条广告
    def queryLastAdverts(self, last_count):
        query = 'select * from ffstore_adverts order by _id desc LIMIT %d ' % last_count
        return DbUtil.query(query)
