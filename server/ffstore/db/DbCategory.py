#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品分类类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
cate_id VARCHAR(50) NOT NULL UNIQUE,
cate_code INT,
cate_logo VARCHAR(200),
cate_name VARCHAR(50)
"""

class DbCategory:

    def __init__(self):
        pass

    @property
    def cate_id(self):
        return self.cate_id

    @property
    def cate_id(self, value):
        self.cate_id = value

    @property
    def cate_code(self):
        return self.cate_code

    @property
    def cate_code(self, value):
        self.cate_code = value

    @property
    def parent_code(self):
        return self.parent_code

    @property
    def parent_code(self, value):
        self.parent_code = value

    @property
    def cate_logo(self):
        return self.cate_logo

    @property
    def cate_logo(self, value):
        self.cate_logo = value

    @property
    def cate_name(self):
        return self.cate_name

    @property
    def cate_name(self, value):
        self.cate_name = value
