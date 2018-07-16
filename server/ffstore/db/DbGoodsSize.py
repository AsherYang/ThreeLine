#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品尺寸类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
goods_id VARCHAR(50),
size_id VARCHAR(50),
goods_size VARCHAR(5)
"""


class DbGoodsSize:

    def __init__(self):
        self._goods_id = None
        self._size_id = None
        self._goods_size = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    @property
    def size_id(self):
        return self._size_id

    @size_id.setter
    def size_id(self, value):
        self._size_id = value

    @property
    def goods_size(self):
        return self._goods_size

    @goods_size.setter
    def goods_size(self, value):
        self._goods_size = value