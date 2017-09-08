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
import json
import time

import DbUtil
import OpenRequest
import TokenConstant
from Token import Token

# import ssl

# get_token_url = "https://oauth.open.weidian.com/token?grant_type=client_credential&appkey=" + TokenConstant.appkey + "&secret=" + TokenConstant.secret
# ssl._create_default_https_context = ssl._create_unverified_context
# 服务型URL
# get_token_url = '%s/oauth2/access_token' % TokenConstant.domain
# 自用型
get_token_url = '%s/token' % TokenConstant.domain


# ====== get 方式 20170907 之前版本，由于微店更改规则，导致直接获取无效，以下面方式模仿浏览器行为 =========
# def getTokenFromNet():
#     # request 封装
#     request = urllib2.Request(url=get_token_url)
#     # 发起请求
#     html = urllib2.urlopen(request)
#     response_data = html.read()
#     print response_data
#     jsonToken = json.loads(response_data)
#     access_token = jsonToken['result']['access_token']
#     expire_in = jsonToken['result']['expire_in']
#     token = Token()
#     token.access_token = access_token
#     token.expire_in = expire_in
#     return token

def getTokenFromNet():
    params = {"appkey": TokenConstant.appkey, "secret": TokenConstant.secret, "grant_type": "client_credential"}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    body = OpenRequest.http_get(get_token_url, params=params, header=header)
    print body
    jsonToken = json.loads(body)
    access_token = jsonToken['result']['access_token']
    expire_in = jsonToken['result']['expire_in']
    token = Token()
    token.access_token = access_token
    token.expire_in = expire_in
    return token


# ====== get token from db ========
def getTokenFromDb():
    query = "select * from sh_token where update_time = (select max(update_time) from sh_token)"
    token = Token()
    results = DbUtil.query(query)
    # print results
    if results is None:
        return None
    for row in results:
        row_id = row[0]
        access_token = row[1]
        expire_in = row[2]
        update_time = row[3]
        token.access_token = access_token
        token.expire_in = expire_in
        token.update_time = update_time
        # print "row_id = %s, access_token = %s, expire_in = %s, update_time = %s " %(row_id, access_token, expire_in, update_time)
    return token


# ====== save token to db =======
def saveToDb(token=None, expire_in=None):
    if token is None or expire_in is None:
        print "token is %s, expire_in is %s" % (token, expire_in)
        return
    else:
        # locattime = time.asctime(time.localtime(time.time()))
        # current_milli_time = lambda: int(round(time.time() * 1000))
        # print locattime
        # print current_milli_time()
        locattime = int(time.time())
        insert = 'insert into sh_token (access_token, expire_in, update_time) values("%s", "%s", "%s")' % (
            token, expire_in, locattime)
        DbUtil.insert(insert)


def doGetToken():
    dbToken = getTokenFromDb()
    currentTime = int(time.time())
    if dbToken is None:
        netToken = getTokenFromNet()
        saveToDb(netToken.access_token, netToken.expire_in)
        print "ok , update token from net success, when dbToken is null. "
        return netToken.access_token
    if currentTime >= int(dbToken.update_time) + int(dbToken.expire_in):
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
