#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品颜色类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
goods_id VARCHAR(50),
size_id VARCHAR(50),
color VARCHAR(10)
"""

class GoodsColor():

    @property
    def goods_id(self):
        return self.goods_id

    @property
    def goods_id(self, value):
        self.goods_id = value

    @property
    def size_id(self):
        return self.size_id

    @property
    def size_id(self, value):
        self.size_id = value

    @property
    def color(self):
        return self.color

    @property
    def color(self, value):
        self.color = value