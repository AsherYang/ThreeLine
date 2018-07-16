#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
goods_id VARCHAR(50) NOT NULL UNIQUE,
cate_id VARCHAR(50),
brand_id VARCHAR(50),
goods_name VARCHAR(150),
market_price INT,
current_price INT NOT NULL,
sale_count INT,
stock_num INT,
goods_code VARCHAR(20),
goods_logo VARCHAR(200),
thum_logo VARCHAR(200),
keywords VARCHAR(200)
"""

class DbGoods:

    def __init__(self):
        self._goods_id = None
        self._cate_id = None
        self._brand_id = None
        self._goods_name = None
        self._market_price = None
        self._current_price = None
        self._sale_count = None
        self._stock_num = None
        self._status = None
        self._goods_code = None
        self._goods_logo = None
        self._thum_logo = None
        self._keywords = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value

    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value

    @property
    def market_price(self):
        return self._market_price

    @market_price.setter
    def market_price(self, value):
        self._market_price = value

    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value

    @property
    def sale_count(self):
        return self._sale_count

    @sale_count.setter
    def sale_count(self, value):
        self._sale_count = value

    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value

    @property
    def goods_logo(self):
        return self._goods_logo

    @goods_logo.setter
    def goods_logo(self, value):
        self._goods_logo = value

    @property
    def thum_logo(self):
        return self._thum_logo

    @thum_logo.setter
    def thum_logo(self, value):
        self._thum_logo = value

    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        self._keywords = value
