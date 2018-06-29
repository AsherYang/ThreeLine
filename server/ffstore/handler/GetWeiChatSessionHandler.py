#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : weichat session tornado handler

api handler
"""

import sys
sys.path.append('../')
import tornado.web
from util.MD5Util import MD5Util, ADMIN_SECRET_KEY
from util.LogUtil import LogUtil
from constant import WxToken
from util import HttpUtil
from FFStoreJsonEncoder import *

"""
获取微信服务器, 登录态 Session
https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code
ffstore 测试appid:wx72877ae8bdff79b0
ffstore 测试appSecret:35c17c2b6f81e7b03735f17f546820bc
参考微信 API 接口, wx.login()

例如:
https://api.weixin.qq.com/sns/jscode2session?appid=wx72877ae8bdff79b0&secret=35c17c2b6f81e7b03735f17f546820bc&js_code=023fYoP02NmKh011uaP02S4rP02fYoP6&grant_type=authorization_code
{"session_key":"yOgupOCOGJ367zpnw14ScQ==","openid":"oUQQ-5bFHPGeXNNgO1mQvEgRLaSY"}
"""
class GetWeiChatSessionHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        jsCode = self.get_argument('jsCode')
        nickName = self.get_argument('nickName')
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        md5Util = MD5Util()
        if sign == md5Util.md5Signature(time):
            logging = LogUtil().getLogging()
            # logging.info('----> jsCode: ' + jsCode)
            # logging.info('----> nickName: ' + nickName)
            # logging.info('----> sign: ' + sign)
            # logging.info('----> time: ' + time)
            httpUrl = 'https://api.weixin.qq.com/sns/jscode2session'
            param = {"appid": WxToken.APP_ID, "secret": WxToken.APP_SECRET,
                     "js_code": str(jsCode), "grant_type": 'authorization_code'}
            body = HttpUtil.http_get(httpUrl, params=param)
            jsonBody = json.loads(body, "utf8")
            if isinstance(jsonBody, dict):
                if jsonBody.has_key('openid'):
                    jsonBody['result'] = True
                else:
                    jsonBody['result'] = False
            # logging.info(type(jsonBody))
            logging.info('--->session json: ' + str(jsonBody))
        else:
            jsonBody = json.loads(u'校验失败', "utf8")
        self.write(jsonBody)
