#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/8.
Desc:   商品
"""

class Goods():

    @property
    def cate_id(self):
        return self.cate_id

    @property
    def cate_id(self, value):
        self.cate_id = value

    @property
    def itemid(self):
        return self.itemid

    @property
    def itemid(self, value):
        self.itemid = value

    @property
    def item_desc(self):
        return self.item_desc

    @property
    def item_desc(self, value):
        self.item_desc = value

    @property
    def item_name(self):
        return self.item_name

    @property
    def item_name(self, value):
        self.item_name = value

    @property
    def imgs(self):
        return self.imgs

    @property
    def imgs(self, value):
        self.imgs = value

    @property
    def price(self):
        return self.price

    @property
    def price(self, value):
        self.price = value

    @property
    def update_time(self):
        return self.update_time

    @property
    def update_time(self, value):
        self.update_time = value