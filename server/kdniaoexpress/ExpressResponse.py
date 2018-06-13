#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/14
Desc:   订单接口返回实体

本类是基础实体, 对应快递鸟接口返回参数
"""


class ExpressResponse:

    def __init__(self):
        pass

    @property
    def msg(self):
        return self.msg

    @property
    def msg(self, value):
        self.msg = value

    @property
    def code_http(self):
        return self.code_http

    @property
    def code_http(self, value):
        self.code_http = value

    @property
    def data(self):
        return self.data

    @property
    def data(self, value):
        self.data = value
