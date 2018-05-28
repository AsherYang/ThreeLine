#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/10
Desc:   操作类型数据库DAO 类
"""
from ffstore.util import DbUtil
from DbCategory import DbCategory


class CategoryDao:
    def __init__(self):
        pass

    def saveToDb(self, cate):
        if isinstance(cate, DbCategory):
            insert = 'insert into ffstore_category (cate_id, cate_code, cate_logo, cate_name) values("%s", "%d", "%s", "%s")' \
                     % (cate.cate_id, cate.cate_code, cate.cate_logo, cate.cate_name)
            print 'insert user to db.'
            return DbUtil.insert(insert)
        return False

    def updateToDb(self, cate):
        if isinstance(cate, DbCategory):
            if not cate.cate_id:
                return False
            if not cate.cate_logo:
                return self.updateNameToDb(cate)
            elif not cate.cate_name:
                return self.updateLogoToDb(cate)
            else:
                update = 'update ffstore_category set cate_logo = "%s", cate_name = "%s" where cate_code = "%s" ' \
                         % (cate.cate_logo, cate.cate_name, cate.cate_code)
                print 'update category logo and name to db'
                return DbUtil.update(update)
        return False

    def updateLogoToDb(self, cate):
        if isinstance(cate, DbCategory):
            update = 'update ffstore_category set cate_logo = "%s" where cate_code = "%s" ' \
                     % (cate.cate_logo, cate.cate_code)
            print 'update category logo to db'
            return DbUtil.update(update)
        return False

    def updateNameToDb(self, cate):
        if isinstance(cate, DbCategory):
            update = 'update ffstore_category set cate_name = "%s" where cate_code = "%s" ' \
                     % (cate.cate_name, cate.cate_code)
            print 'update category name to db'
            return DbUtil.update(update)
        return False

    def saveOrUpdateToDb(self, cate):
        if isinstance(cate, DbCategory):
            category = self.queryCateById(cate.cate_id)
            if category:
                return self.updateToDb(cate)
            else:
                return self.saveToDb(cate)
        return False

    def deleteFromDb(self, cate):
        if isinstance(cate, DbCategory):
            delete = 'delete from ffstore_category where cate_code = "%s" ' % cate.cate_code
            print 'delete category:%s from db.' % cate.cate_code
            return DbUtil.delete(delete)
        return False

    def queryAllCateFromDb(self):
        query = 'select * from ffstore_category'
        return DbUtil.query(query)

    # 根据显示类型查询分类, 分页查询
    def queryCateListByShowType(self, cateShowType=0, page_num=1, page_size=10):
        start = (page_num - 1) * page_size
        query = 'select * from ffstore_category where cate_show_type = "%s" order by _id asc limit %s, %s;' \
                % (cateShowType, start, page_size)
        return DbUtil.query(query)

    def queryCateCountByShowType(self, cateShowType=0):
        query = 'select count(*) from ffstore_category where cate_show_type = "%s"' % cateShowType
        return DbUtil.query(query)

    # 根据分类ID查询对应分类
    def queryCateById(self, cateId):
        if not cateId:
            return None
        query = 'select * from ffstore_category where cate_id = "%s"' % cateId
        return DbUtil.query(query)
