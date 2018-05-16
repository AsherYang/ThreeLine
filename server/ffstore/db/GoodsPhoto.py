#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品详情图片类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
goods_id VARCHAR(50),
photo VARCHAR(200),
thum_photo VARCHAR(200)
"""

class GoodsPhoto():

    @property
    def goods_id(self):
        return self.goods_id

    @property
    def goods_id(self, value):
        self.goods_id = value

    @property
    def photo(self):
        return self.photo

    @property
    def photo(self, value):
        self.photo = value

    @property
    def thum_photo(self):
        return self.thum_photo

    @property
    def thum_photo(self, value):
        self.thum_photo = value
