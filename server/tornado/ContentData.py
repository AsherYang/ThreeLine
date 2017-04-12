#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   Content to response to client
"""

from BaseResponse import BaseResponse

# extends BaseResponse
class ContentData(BaseResponse):

    @property
    def syncKey(self):
        return self.syncKey

    @property
    def syncKey(self, value):
        self.syncKey = value

    @property
    def updateTime(self):
        return self.createTime

    @property
    def updateTime(self, value):
        self.createTime = value