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
thum_logo VARCHAR(200)
"""

class DbGoods:

    def __init__(self):
        pass

    @property
    def goods_id(self):
        return self.goods_id

    @property
    def goods_id(self, value):
        self.goods_id = value

    @property
    def cate_id(self):
        return self.cate_id

    @property
    def cate_id(self, value):
        self.cate_id = value

    @property
    def brand_id(self):
        return self.brand_id

    @property
    def brand_id(self, value):
        self.brand_id = value

    @property
    def goods_name(self):
        return self.goods_name

    @property
    def goods_name(self, value):
        self.goods_name = value

    @property
    def market_price(self):
        return self.market_price

    @property
    def market_price(self, value):
        self.market_price = value

    @property
    def current_price(self):
        return self.current_price

    @property
    def current_price(self, value):
        self.current_price = value

    @property
    def sale_count(self):
        return self.sale_count

    @property
    def sale_count(self, value):
        self.sale_count = value

    @property
    def stock_num(self):
        return self.stock_num

    @property
    def stock_num(self, value):
        self.stock_num = value

    @property
    def status(self):
        return self.status

    @property
    def status(self, value):
        self.status = value

    @property
    def goods_code(self):
        return self.goods_code

    @property
    def goods_code(self, value):
        self.goods_code = value

    @property
    def goods_logo(self):
        return self.goods_logo

    @property
    def goods_logo(self, value):
        self.goods_logo = value

    @property
    def thum_logo(self):
        return self.thum_logo

    @property
    def thum_logo(self, value):
        self.thum_logo = value