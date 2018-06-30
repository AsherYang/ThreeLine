#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/30
Desc  : 将 wxpy 生成的登录二维码通过浏览器API返回出去，便于登录
"""
import sys
sys.path.append('../')
import tornado.web


# todo remove
class ManagerLoadWxQrCodeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        pass