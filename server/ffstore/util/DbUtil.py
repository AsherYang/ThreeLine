#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/8.
Desc:  database util
"""
import sys

sys.path.append('../')

import MySQLdb

from constant import DbConstant


def getDb():
    db = MySQLdb.connect(DbConstant.dbHost, DbConstant.dbUser, DbConstant.dbPwd, DbConstant.dbName)
    db.set_character_set('utf8')
    return db


def getConn(db):
    if db is None:
        return None
    cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    return cursor


def insert(sql=None):
    if sql is None:
        return False
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return False
    try:
        # "None" 替换为 NULL , 结合数据Dao values("%s", "%s", "%s"）双引号的写法
        # 此种方式可以将NULL 赋值给未设定的mysql Int 型
        sql = sql.replace('"None"', 'NULL').replace('"none"', 'NULL').replace('"nan"', 'NULL')
        cursor.execute(sql)
        db.commit()
        print 'save data ToDb success ! '
        return True
    except Exception as e:
        print "saveToDb except "
        print e
        db.rollback()
    finally:
        cursor.close()
        db.close()
    return False


def query(sql=None):
    if sql is None:
        return None
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return None
    try:
        sql = sql.replace('"None"', 'NULL').replace('"none"', 'NULL').replace('"nan"', 'NULL')
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            # print results
            return results
        else:
            print " database is empty !"
            return None
    except Exception as e:
        print "query except "
        print e
    finally:
        cursor.close()
        db.close()
    return None


def queryByArgs(sql=None, args=None):
    if sql is None:
        return None
    if args is None:
        return query(sql)
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return None
    try:
        sql = sql.replace('"None"', 'NULL').replace('"none"', 'NULL').replace('"nan"', 'NULL')
        cursor.execute(sql, args)
        results = cursor.fetchall()
        if results:
            # print results
            return results
        else:
            print " database is empty !"
            return None
    except Exception as e:
        print "query except "
        print e
    finally:
        cursor.close()
        db.close()
    return None


def querySingleRow(sql=None):
    if sql is None:
        return None
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return None
    try:
        sql = sql.replace('"None"', 'NULL').replace('"none"', 'NULL').replace('"nan"', 'NULL')
        cursor.execute(sql)
        results = cursor.fetchone()
        if results:
            # print results
            return results
        else:
            print " database is empty !"
            return None
    except Exception as e:
        print "query except "
        print e
    finally:
        cursor.close()
        db.close()
    return None


def update(sql=None):
    if sql is None:
        return False
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return False
    try:
        sql = sql.replace('"None"', 'NULL').replace('"none"', 'NULL').replace('"nan"', 'NULL')
        cursor.execute(sql)
        # 更新和插入一样，需要commit
        db.commit()
        print 'update success !'
        return True
    except Exception as e:
        print "update except "
        print e
        # 操作失败，需要回滚
        db.rollback()
    finally:
        cursor.close()
        db.close()
    return False


def delete(sql=None):
    if sql is None:
        return False
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return False
    try:
        sql = sql.replace('"None"', 'NULL').replace('"none"', 'NULL').replace('"nan"', 'NULL')
        cursor.execute(sql)
        # 删除和插入一样，需要commit
        db.commit()
        print 'delete success !'
        return True
    except Exception as e:
        print "delete except "
        print e
        # 操作失败，需要回滚
        db.rollback()
    finally:
        cursor.close()
        db.close()
    return False
