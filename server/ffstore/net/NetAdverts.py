#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 广告,banner 网络实体
"""


class NetAdverts:

    def __init__(self):
        pass

    # 对应db advert_id
    @property
    def id(self):
        return self.id

    @property
    def id(self, value):
        self.id = value

    @property
    def advertUrl(self):
        return self.advertUrl

    @property
    def advertUrl(self, value):
        self.advertUrl = value

    @property
    def picUrl(self):
        return self.picUrl

    @property
    def picUrl(self, value):
        self.picUrl = value

    @property
    def sort(self):
        return self.sort

    @property
    def sort(self, value):
        self.sort = value

    @property
    def title(self):
        return self.title

    @property
    def title(self, value):
        self.title = value

    @property
    def createTime(self):
        return self.createTime

    @property
    def createTime(self, value):
        self.createTime = value