#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   属性类，包括分类属性，商品详情属性

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
cate_id VARCHAR(50),
goods_id VARCHAR(50),
attr_brand_name VARCHAR(50),
attr_market_year VARCHAR(20),
attr_size VARCHAR(5),
attr_color VARCHAR(5)
"""


class DbAttribute:
    def __init__(self):
        pass

    @property
    def cate_id(self):
        return self.cate_id

    @property
    def cate_id(self, value):
        self.cate_id = value

    @property
    def goods_id(self):
        return self.goods_id

    @property
    def goods_id(self, value):
        self.goods_id = value

    @property
    def attr_brand_name(self):
        return self.attr_brand_name

    @property
    def attr_brand_name(self, value):
        self.attr_brand_name = value

    @property
    def attr_market_year(self):
        return self.attr_market_year

    @property
    def attr_market_year(self, value):
        self.attr_market_year = value

    @property
    def attr_size(self):
        return self.attr_size

    @property
    def attr_size(self, value):
        self.attr_size = value

    @property
    def attr_color(self):
        return self.attr_color

    @property
    def attr_color(self, value):
        self.attr_color = value
