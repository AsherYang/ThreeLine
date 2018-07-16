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
        self._brand_id = None
        self._brand_name = None
        self._brand_logo = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value

    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
