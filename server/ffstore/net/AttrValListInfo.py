#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/1
Desc:   首页封面实体 attrValList 实体
作为 {@see AttrsInfo#Attrs} 的子类(集合形式)

/**
 * attrName : 品牌
 * attrNameId : 213
 * attrVal : 素洁
 * id : 556
 */
"""

class AttrValList:

    def __init__(self):
        pass

    @property
    def attrName(self):
        return self.attrName

    @property
    def attrName(self, value):
        self.attrName = value

    @property
    def attrNameId(self):
        return self.attrNameId

    @property
    def attrNameId(self, value):
        self.attrNameId = value

    @property
    def attrVal(self):
        return self.attrVal

    @property
    def attrVal(self, value):
        self.attrVal = value

    @property
    def id(self):
        return self.id

    @property
    def id(self, value):
        self.id = value