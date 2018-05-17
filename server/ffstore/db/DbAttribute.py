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
attr_name VARCHAR(50),
attr_val VARCHAR(150)
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
    def attr_name(self):
        return self.attr_name

    @property
    def attr_name(self, value):
        self.attr_name = value

    @property
    def attr_val(self):
        return self.attr_val

    @property
    def attr_val(self, value):
        self.attr_val = value

