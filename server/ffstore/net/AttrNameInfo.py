#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/1
Desc:   首页封面实体 attrName 实体
作为 {@see AttrsInfo#Attrs} 的子类

/**
 * attrName : 品牌
 * categoryCode : 022
 * id : 213
 */
"""

class AttrName():

    @property
    def attrName(self):
        return self.attrName

    @property
    def attrName(self, value):
        self.attrName = value

    @property
    def categoryCode(self):
        return self.categoryCode

    @property
    def categoryCode(self, value):
        self.categoryCode = value

    @property
    def id(self):
        return self.id

    @property
    def id(self, value):
        self.id = value