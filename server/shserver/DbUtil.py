#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/8.
Desc:  database util
"""
import MySQLdb

import DbConstant


def getDb():
    db = MySQLdb.connect(DbConstant.dbHost, DbConstant.dbUser, DbConstant.dbPwd, DbConstant.dbName)
    db.set_character_set('utf8')
    return db


def getConn(db):
    if db is None:
        return None
    cursor = db.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    return cursor


def insert(sql=None):
    if sql is None:
        return
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return
    try:
        cursor.execute(sql)
        db.commit()
        print 'save data ToDb success ! '
    except Exception as e:
        print "saveToDb except "
        print e
        db.rollback()
    cursor.close()
    db.close()


def query(sql=None):
    if sql is None:
        return None
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return None
    try:
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
    cursor.close()
    db.close()
    return None


def delete(sql=None):
    if sql is None:
        return
    db = getDb()
    cursor = getConn(db)
    if cursor is None:
        db.close()
        return
    try:
        cursor.execute(sql)
        # 删除和插入一样，需要commit
        db.commit()
        print 'delete success !'
    except Exception as e:
        print "delete except "
        print e
        # 操作失败，需要回滚
        db.rollback()
    cursor.close()
    db.close()
    return
