#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   base content to response to client
"""

# extends BaseResponse
class BaseResponse():

    def __init__(self):
        self.code = '200'
        self.desc = ''
        self.data = ''

    @property
    def code(self):
        return self.code

    @property
    def code(self, value):
        self.code = value

    @property
    def desc(self):
        return self.desc

    @property
    def desc(self, value):
        self.desc = value


