#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/8.
Desc:
"""

class Category():

    @property
    def cate_id(self):
        return self.cate_id

    @property
    def cate_id(self, value):
        self.cate_id = value

    @property
    def cate_name(self):
        return self.cate_name

    @property
    def cate_name(self, value):
        self.cate_name = value

    @property
    def parent_id(self):
        return self.parent_id

    @property
    def parent_id(self, value):
        self.parent_id = value

    @property
    def parent_cate_name(self):
        return self.parent_cate_name

    @property
    def parent_cate_name(self, value):
        self.parent_cate_name = value

    @property
    def sort_num(self):
        return self.sort_num

    @property
    def sort_num(self, value):
        self.sort_num = value

    @property
    def cate_item_num(self):
        return self.cate_item_num

    @property
    def cate_item_num(self, value):
        self.cate_item_num = value

    @property
    def description(self):
        return self.description

    @property
    def description(self, value):
        self.description = value

    @property
    def listUrl(self):
        return self.listUrl

    @property
    def listUrl(self, value):
        self.listUrl = value

    @property
    def shopName(self):
        return self.shopName

    @property
    def shopName(self, value):
        self.shopName = value

    @property
    def shopLogo(self):
        return self.shopLogo

    @property
    def shopLogo(self, value):
        self.shopLogo = value

    @property
    def update_time(self):
        return self.update_time

    @property
    def update_time(self, value):
        self.update_time = value