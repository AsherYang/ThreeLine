#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2017/11/22
Desc  : sina weibo crawler
@see  :  http://open.weibo.com/tools/console
使用文档中"授权机制" -> "开发者自身的授权" -> "接口测试工具"(Token 也是此自身授权)
需要区分OAuth2.0授权： 是指应用需要用户授权用户的新浪微博权限给应用，可用来读取授权用户的微博信息。
此处，我们只是用自己的授权，即开发者自身的授权，用于读取自身的微博数据。
"""

from TokenConstant import *

BASE_URL = sina_domain
# NEW_PUSH_URL = BASE_URL + 'statuses/user_timeline.json'
# TOKEN_URL = BASE_URL + 'OAuth2/authorize'

class SinaWbCrawler() :
    def __init__(self):
        print 'sina weibo crawler.'

    def do(self):
        return self.getAccessToken()

    def getAccessToken(self):
        return sina_token

if __name__ == '__main__':
    sinaWbCrawler = SinaWbCrawler()
    print sinaWbCrawler.do()