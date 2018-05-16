#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/1
Desc:   首页封面实体 attrs 实体
作为 {@see DiscoverInfo#Discover} 的子类(集合形式)

/**
 * attrValList : [{"attrName":"品牌","attrNameId":213,"attrVal":"素洁","id":556}]
 * attrName : {"attrName":"品牌","categoryCode":"022","id":213}
 */
"""

class Attrs():

    @property
    def attrValList(self):
        return self.attrValList

    @property
    def attrValList(self, value):
        self.attrValList = value

    @property
    def attrName(self):
        return self.attrName

    @property
    def attrName(self, value):
        self.attrName = value

    def append(self, value):
        return self.attrValList + [value]

    # extend 只能是一个列表
    def extend(self, value):
        return self.attrValList.extend(value)