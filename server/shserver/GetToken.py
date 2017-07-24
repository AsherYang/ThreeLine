#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   get weidian token
@see https://wiki.open.weidian.com/guide#145

https://oauth.open.weidian.com/token?grant_type=client_credential&appkey=xxx&secret=xxx
必须为get 请求
"""
import TokenConstant
import urllib2
import json
import time
import MySQLdb
import DbConstant
from Token import Token

get_token_url = "https://oauth.open.weidian.com/token?grant_type=client_credential&appkey=" + TokenConstant.appkey + "&secret=" + TokenConstant.secret

# ====== get 方式 =========
def getTokenFromNet():
    # request 封装
    request = urllib2.Request(url=get_token_url)
    # 发起请求
    html = urllib2.urlopen(request)
    response_data = html.read()
    print response_data
    jsonToken = json.loads(response_data)
    access_token = jsonToken['result']['access_token']
    expire_in = jsonToken['result']['expire_in']
    token = Token()
    token.access_token = access_token
    token.expire_in = expire_in
    return token

# ====== get token from db ========
def getTokenFromDb():
    db = MySQLdb.connect(DbConstant.dbHost, DbConstant.dbUser, DbConstant.dbPwd, DbConstant.dbName)
    cursor = db.cursor()
    query = "select * from sh_token where update_time = (select max(update_time) from sh_token)"
    token = Token()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print "result = %s " %(results)
        if results:
            for row in results:
                row_id = row[0]
                access_token = row[1]
                expire_in = row[2]
                update_time = row[3]
                token.access_token = access_token
                token.expire_in = expire_in
                token.update_time = update_time
            # print "row_id = %s, access_token = %s, expire_in = %s, update_time = %s " %(row_id, access_token, expire_in, update_time)
        else:
            print "getTokenFromDb result is null. "
            return None
    except:
        print "getTokenFromDb except"
        return None
    db.close()
    return token

# ====== save token to db =======
def saveToDb(token=None, expire_in=None):
    if token is None or expire_in is None:
        print "token is %s, expire_in is %s" %(token, expire_in)
        return
    else:
        # locattime = time.asctime(time.localtime(time.time()))
        # current_milli_time = lambda: int(round(time.time() * 1000))
        # print locattime
        # print current_milli_time()
        locattime = int(time.time())
        db = MySQLdb.connect(DbConstant.dbHost, DbConstant.dbUser, DbConstant.dbPwd, DbConstant.dbName)
        cursor = db.cursor()
        insert = 'insert into sh_token (access_token, expire_in, update_time) values("%s", "%s", "%s")' %(token, expire_in, locattime)
        try:
            cursor.execute(insert)
            db.commit()
        except:
            print "saveToDb except"
            db.rollback()
        cursor.close()

def doGetToken():
    dbToken = getTokenFromDb()
    currentTime = int(time.time())
    if dbToken is None:
        netToken = getTokenFromNet()
        saveToDb(netToken.access_token, netToken.expire_in)
        print "ok , update token from net success, when dbToken is null. "
        return netToken.access_token
    elif currentTime >= int(dbToken.update_time) + int(dbToken.expire_in):
        print "currentTime = %s , update_time = %s " % (currentTime, dbToken.update_time)
        # expired
        netToken = getTokenFromNet()
        saveToDb(netToken.access_token, netToken.expire_in)
        print "ok , update token from net success. "
        return netToken.access_token
    else:
        print "ok , token in date. "
        return dbToken.access_token

if __name__ == '__main__':
    doGetToken()
