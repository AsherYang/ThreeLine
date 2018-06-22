#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   base content to response to client

code : 返回状态码
desc : 返回状态码描述
pageNum    : 分页时，所在页码
pageSize   : 分页时，每页大小
page_total : 分页时，分页总数
totalCount : 分页时，数据总量
data       : 返回的具体数据
"""
from constant import ResponseCode


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
    def pageNum(self):
        return self.pageNum

    @property
    def pageNum(self, value):
        self.pageNum = value

    @property
    def pageSize(self):
        return self.pageSize

    @property
    def pageSize(self, value):
        self.pageSize = value

    @property
    def page_total(self):
        return self.page_total

    @property
    def page_total(self, value):
        self.page_total = value

    @property
    def totalCount(self):
        return self.totalCount

    @property
    def totalCount(self, value):
        self.totalCount = value

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
