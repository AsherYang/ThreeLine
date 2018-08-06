#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/8/02
Desc  : 商品图片 网络实体
"""


class NetGoodPhoto:

    def __init__(self):
        self._goods_id = None
        self._photo = None
        self._thum_photo = None

    # 对应db advert_id
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value

    @property
    def thum_photo(self):
        return self._thum_photo

    @thum_photo.setter
    def thum_photo(self, value):
        self._thum_photo = value
