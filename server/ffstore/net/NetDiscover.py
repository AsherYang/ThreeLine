#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/1
Desc:   首页封面实体

/**
 * code : 022 ---> categoryCode
 * logo : http://sujiefs.com/upload/images/20180322/201803221134300716543.jpg
 * id : 2c9257a16126d14701612b52808100d6
 * attrs : [{"attrValList":[{"attrName":"品牌","attrNameId":213,"attrVal":"素洁","id":556}],"attrName":{"attrName":"品牌","categoryCode":"022","id":213}},{"attrValList":[{"attrName":"年份季节","attrNameId":214,"attrVal":"2018春季新款","id":557}],"attrName":{"attrName":"年份季节","categoryCode":"022","id":214}}]
 */
"""


class NetDiscover:
    def __init__(self):
        self._id = None
        self._code = None
        self._logo = None
        self._brand_name = None
        self._attr_market_year = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value

    @property
    def attr_market_year(self):
        return self._attr_market_year

    @attr_market_year.setter
    def attr_market_year(self, value):
        self._attr_market_year = value
