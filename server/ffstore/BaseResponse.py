#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   base content to response to client
"""
from ffstore.constant import ResponseCode

# extends BaseResponse
class BaseResponse:
    # define init method
    def __init__(self):
        self.code = ResponseCode.op_success
        self.desc = ResponseCode.op_success_desc
        self.data = []

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

    @property
    def data(self):
        return self.data

    @property
    def data(self, value):
        self.data = value

    # append to data,
    # @see http://stackoverflow.com/questions/16380575/python-decorating-property-setter-with-list
    def append(self, value):
        return self.data + [value]

    # extend 只能是一个列表
    def extend(self, value):
        return self.data.extend(value)
