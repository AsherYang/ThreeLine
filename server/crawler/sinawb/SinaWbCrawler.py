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
import json

BASE_URL = sina_domain
# 返回最新的公共微博 {@link http://open.weibo.com/wiki/2/statuses/public_timeline}
NEW_PUBLIC_URL = BASE_URL + 'statuses/public_timeline.json'
POST_BY_ME_URL = BASE_URL + 'statuses/repost_by_me.json'
FRIEND_POST_IDS_URL = BASE_URL + 'statuses/friends_timeline/ids.json'
USER_POST_IDS_URL = BASE_URL + 'statuses/user_timeline/ids.json'
SHOW_CONTENT_URL = BASE_URL + 'statuses/show.json'

class SinaWbCrawler() :
    def __init__(self):
        print 'sina weibo crawler.'

    # 返回最新的公共微博
    def getNewPublic(self, public_url, count=100, page=1, base_app=0):
        token = self.getAccessToken()
        # url = "%s?access_token=%s" % (public_url, token)
        param = {"access_token": token, "count": count, "page": page, "base_app": base_app}
        body = SinaHttpUtil.http_get(public_url, param, header={})
        return body

    # 获取当前用户最新转发的微博列表
    def getRepostByMe(self, url, since_id=0, max_id=0, count=20, page=1):
        token = self.getAccessToken()
        param = {'access_token': token, 'since_id': since_id, 'max_id': max_id, 'count': count, 'page':page}
        body = SinaHttpUtil.http_get(url, param, header={})
        return body

    # 获取当前登录用户及其所关注用户的最新微博的ID
    def getFriendPostIds(self, url, since_id=0, max_id=0, count=20, page=1, base_app=0, feature=0):
        token = self.getAccessToken()
        param = {'access_token': token, 'since_id': since_id, 'max_id': max_id, 'count': count, 'page': page,
                 'base_app': base_app, 'feature':feature}
        body = SinaHttpUtil.http_get(url, param, header={})
        return body

    # 获取用户发布的微博的ID
    def getUserPostIds(self, url, uid=None, screen_name=None, since_id=0, max_id=0, count=20, page=1, base_app=0, feature=0):
        token = self.getAccessToken()
        if uid is None or screen_name is None:
            param = {'access_token': token, 'since_id': since_id, 'max_id': max_id,
                     'count': count, 'page': page,'base_app': base_app, 'feature': feature}
        else:
            param = {'access_token': token, 'uid':uid, 'screen_name':screen_name, 'since_id': since_id, 'max_id': max_id,
                     'count': count, 'page': page, 'base_app': base_app, 'feature': feature}
        body = SinaHttpUtil.http_get(url, param, header={})
        return body

    # 根据微博ID获取单条微博内容
    def getContentById(self, url, weibo_id):
        token = self.getAccessToken()
        param = {'access_token': token, 'id': weibo_id}
        body = SinaHttpUtil.http_get(url, param, header={})
        jsonBody = json.loads(body, "utf8")
        # return body
        str = "%s create at % s" %(jsonBody['text'], jsonBody['created_at'])
        return str

    # 获取 accessToken， 这里使用的是开发者自身的授权
    def getAccessToken(self):
        return sina_token

if __name__ == '__main__':
    sinaWbCrawler = SinaWbCrawler()
    # print sinaWbCrawler.getNewPublic(NEW_PUBLIC_URL)
    # print sinaWbCrawler.getRepostByMe(POST_BY_ME_URL)
    # print sinaWbCrawler.getFriendPostIds(FRIEND_POST_IDS_URL)
    print sinaWbCrawler.getUserPostIds(USER_POST_IDS_URL)
    print sinaWbCrawler.getContentById(SHOW_CONTENT_URL, '4176845702748333')