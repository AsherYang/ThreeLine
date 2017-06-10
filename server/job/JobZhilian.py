#! /usr/bin/python
# - * - coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import lxml.html
import pprint

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/5/23
Desc:   智联招聘类
"""
ZHILIAN_HOST_URL = 'https://www.zhaopin.com/'
ZHILIAN_LOGIN_URL = ''

class ZhilianJob():

    def __init__(self):
        self.name = ''
        self.pwd = ''
        self.cj = ''
        self.handler = ''
        self.opener = ''

    def initCookie(self):
        self.cj = cookielib.CookieJar()
        self.handler = urllib2.HTTPCookieProcessor(self.cj)
        self.opener = urllib2.build_opener(self.handler)

    def parse_form(self, html):
        tree = lxml.html.fromstring(html)
        data = {}
        for e in tree.cssselect('form input'):
            if e.get('name'):
                data[e.get('name')] = e.get('value')
        return data

    def login(self):
        self.initCookie()
        html = self.opener.open(ZHILIAN_HOST_URL).read()
        data = self.parse_form(html)
        data['loginname'] = self.name
        data['Password'] = self.pwd
        pprint.pprint(data)
        
        return

