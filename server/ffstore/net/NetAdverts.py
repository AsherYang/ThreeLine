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
        self._id = None
        self._advertUrl = None
        self._picUrl = None
        self._sort = None
        self._title = None
        self._createTime = None

    # 对应db advert_id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def advertUrl(self):
        return self._advertUrl

    @advertUrl.setter
    def advertUrl(self, value):
        self._advertUrl = value

    @property
    def picUrl(self):
        return self._picUrl

    @picUrl.setter
    def picUrl(self, value):
        self._picUrl = value

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def createTime(self):
        return self._createTime

    @createTime.setter
    def createTime(self, value):
        self._createTime = value