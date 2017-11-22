#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2017/11/22
Desc  : sina weibo crawler
@see  :  http://open.weibo.com/tools/console
1. 使用文档中"授权机制" -> "开发者自身的授权" -> "接口测试工具"(Token 也是此自身授权)
需要区分OAuth2.0授权： 是指应用需要用户授权用户的新浪微博权限给应用，可用来读取授权用户的微博信息。
此处，我们只是用自己的授权，即开发者自身的授权，用于读取自身的微博数据。
2. 关于已获取的接口权限：可查看 "我的应用" -> "接口管理"
3. 通过结合 "已有接口" 加上 "API 测试工具"， 可在线调试接口
"""

from TokenConstant import *
import SinaHttpUtil

BASE_URL = sina_domain
# 返回最新的公共微博 {@link http://open.weibo.com/wiki/2/statuses/public_timeline}
NEW_PUBLIC_URL = BASE_URL + 'statuses/public_timeline.json'

class SinaWbCrawler() :
    def __init__(self):
        print 'sina weibo crawler.'

    def getNewPublic(self, public_url, count=100, page=1, base_app=0):
        token = self.getAccessToken()
        # url = "%s?access_token=%s" % (public_url, token)
        param = {"access_token": token, "count": count, "page": page, "base_app": base_app}
        body = SinaHttpUtil.http_get(public_url, param, header={})
        return body

    def getAccessToken(self):
        return sina_token

if __name__ == '__main__':
    sinaWbCrawler = SinaWbCrawler()
    print sinaWbCrawler.getNewPublic(NEW_PUBLIC_URL)