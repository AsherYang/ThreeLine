#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   厂家（品牌）类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
brand_id VARCHAR(50),
brand_name VARCHAR(30),
brand_logo VARCHAR(200)
"""

class DbBrand:

    def __init__(self):
        pass

    @property
    def brand_id(self):
        return self.brand_id

    @property
    def brand_id(self, value):
        self.brand_id = value

    @property
    def brand_name(self):
        return self.brand_name

    @property
    def brand_name(self, value):
        self.brand_name = value

    @property
    def brand_logo(self):
        return self.brand_logo

    @property
    def brand_logo(self, value):
        self.brand_logo = value
