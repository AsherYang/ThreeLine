#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/26
Desc  : 广告(banner)类
"""


class DbAdverts:
    def __init__(self):
        pass

    @property
    def advert_id(self):
        return self.advert_id

    @property
    def advert_id(self, value):
        self.advert_id = value

    @property
    def cate_id(self):
        return self.cate_id

    @property
    def cate_id(self, value):
        self.cate_id = value

    @property
    def title(self):
        return self.title

    @property
    def title(self, value):
        self.title = value

    @property
    def pic_url(self):
        return self.pic_url

    @property
    def pic_url(self, value):
        self.pic_url = value

    @property
    def sort(self):
        return self.sort

    @property
    def sort(self, value):
        self.sort = value

    @property
    def create_time(self):
        return self.create_time

    @property
    def create_time(self, value):
        self.create_time = value