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
attr_market_year VARCHAR(20),
attr_size VARCHAR(5),
attr_color VARCHAR(10),
foreign key (goods_id) references ffstore_goods(goods_id) on delete cascade on update cascade
"""


class DbAttribute:
    def __init__(self):
        self._cate_id = None
        self._goods_id = None
        self._attr_market_year = None
        self._attr_size = None
        self._attr_color = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    @property
    def attr_market_year(self):
        return self._attr_market_year

    @attr_market_year.setter
    def attr_market_year(self, value):
        self._attr_market_year = value

    @property
    def attr_size(self):
        return self._attr_size

    @attr_size.setter
    def attr_size(self, value):
        self._attr_size = value

    @property
    def attr_color(self):
        return self._attr_color

    @attr_color.setter
    def attr_color(self, value):
        self._attr_color = value

