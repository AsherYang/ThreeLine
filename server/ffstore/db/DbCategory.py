#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品分类类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
cate_id VARCHAR(50) NOT NULL UNIQUE,
cate_code INT NOT NULL UNIQUE,
parent_code INT,
cate_logo VARCHAR(200),
cate_name VARCHAR(50),
cate_show_type VARCHAR(3) DEFAULT 0
"""


class DbCategory:
    def __init__(self):
        self._cate_id = None
        self._cate_code = None
        self._parent_code = None
        self._cate_logo = None
        self._cate_name = None
        self._cate_show_type = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value

    @property
    def cate_code(self):
        return self._cate_code

    @cate_code.setter
    def cate_code(self, value):
        self._cate_code = value

    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value

    @property
    def cate_logo(self):
        return self._cate_logo

    @cate_logo.setter
    def cate_logo(self, value):
        self._cate_logo = value

    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value

    @property
    def cate_show_type(self):
        return self._cate_show_type

    @cate_show_type.setter
    def cate_show_type(self, value):
        self._cate_show_type = value
