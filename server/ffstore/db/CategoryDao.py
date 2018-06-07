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
from ffstore.constant import CategoryShowType


class CategoryDao:
    def __init__(self):
        pass

    def saveToDb(self, cate):
        if isinstance(cate, DbCategory):
            insert = 'insert into ffstore_category (cate_id, cate_code, parent_code, cate_logo, cate_name, cate_show_type)' \
                     ' values("%s", "%d", "%d", "%s", "%s", "%s")' \
                     % (cate.cate_id, cate.cate_code, cate.parent_code, cate.cate_logo, cate.cate_name, cate.cate_show_type)
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

    # 更新category log
    def updateLogoToDb(self, cate):
        if isinstance(cate, DbCategory):
            update = 'update ffstore_category set cate_logo = "%s" where cate_code = "%s" ' \
                     % (cate.cate_logo, cate.cate_code)
            print 'update category logo to db'
            return DbUtil.update(update)
        return False

    # 更新category name
    def updateNameToDb(self, cate):
        if isinstance(cate, DbCategory):
            update = 'update ffstore_category set cate_name = "%s" where cate_code = "%s" ' \
                     % (cate.cate_name, cate.cate_code)
            print 'update category name to db'
            return DbUtil.update(update)
        return False

    # 更新category cate_show_type, {@see CategoryShowType}默认为0:表示一般展示类型，1: 首页展示；
    def updateShowTypeToDb(self, cate):
        if isinstance(cate, DbCategory):
            update = 'update ffstore_category set cate_show_type = "%s" where cate_code = "%s" ' \
                     % (cate.cate_show_type, cate.cate_code)
            print 'update category cate show type to db'
            return DbUtil.update(update)
        return False

    # 更新category code
    def updateCodeToDb(self, old_code, new_code):
        if not old_code or not new_code:
            return False
        update = 'update ffstore_category set cate_code = "%s" where cate_code = "%s" ' \
                 % (new_code, old_code)
        print 'update category code to db'
        return DbUtil.update(update)

    def saveOrUpdateToDb(self, cate):
        if isinstance(cate, DbCategory):
            category = self.queryCateById(cate.cate_id)
            if category:
                return self.updateToDb(cate)
            else:
                return self.saveToDb(cate)
        return False

    def deleteCate(self, cate):
        if isinstance(cate, DbCategory):
            delete = 'delete from ffstore_category where cate_code = "%s" ' % cate.cate_code
            print 'delete category:%s from db.' % cate
            return DbUtil.delete(delete)
        return False

    def deleteByCateId(self, cate_id):
        delete = 'delete from ffstore_category where cate_id = "%s" ' % cate_id
        print 'delete category by cate_id:%s from db.' % cate_id
        return DbUtil.delete(delete)

    def deleteByCateCode(self, cate_code):
        delete = 'delete from ffstore_category where cate_code = "%s" ' % cate_code
        print 'delete category by cate_code:%s from db.' % cate_code
        return DbUtil.delete(delete)

    def queryAllCateFromDb(self):
        query = 'select * from ffstore_category'
        return DbUtil.query(query)

    # 根据显示类型查询分类, 分页查询
    def queryCateListByShowType(self, cateShowType=CategoryShowType.TYPE_SHOW_NORMAL, page_num=1, page_size=10):
        start = (page_num - 1) * page_size
        query = 'select * from ffstore_category where cate_show_type = "%s" order by _id asc limit %s, %s;' \
                % (cateShowType, start, page_size)
        return DbUtil.query(query)

    # 查询对应showType下的分类总数
    def queryCateCountByShowType(self, cateShowType=0):
        query = 'select count(*) from ffstore_category where cate_show_type = "%s"' % cateShowType
        return DbUtil.query(query)

    # 根据分类ID查询对应分类
    def queryCateById(self, cateId):
        if not cateId:
            return None
        query = 'select * from ffstore_category where cate_id = "%s"' % cateId
        return DbUtil.query(query)

    # 根据分类编码code查询对应分类
    def queryCateByCode(self, cateCode):
        if not cateCode:
            return None
        query = 'select * from ffstore_category where cate_code = "%s"' % cateCode
        return DbUtil.query(query)
