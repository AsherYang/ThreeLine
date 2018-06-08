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
        pass

    @property
    def code(self):
        return self.code

    @property
    def code(self, value):
        self.code = value

    @property
    def logo(self):
        return self.logo

    @property
    def logo(self, value):
        self.logo = value

    @property
    def id(self):
        return self.id

    @property
    def id(self, value):
        self.id = value

    @property
    def brand_name(self):
        return self.brand_name

    @property
    def brand_name(self, value):
        self.brand_name = value

    @property
    def attr_market_year(self):
        return self.attr_market_year

    @property
    def attr_market_year(self, value):
        self.attr_market_year = value
