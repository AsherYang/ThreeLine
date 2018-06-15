#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/15
Desc:   时间工具类
"""

import datetime

class DateUtil:

    def __init__(self):
        pass

    def getCurrentTime(self):
        return datetime.datetime.now()


if __name__ == '__main__':
    dateUtil = DateUtil()
    print dateUtil.getCurrentTime()
