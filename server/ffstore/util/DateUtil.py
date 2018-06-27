#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/15
Desc:   时间工具类
"""

import datetime
import time

class DateUtil:

    def __init__(self):
        pass

    def getCurrentTime(self):
        return datetime.datetime.now()

    def getCurrentTimeStamp(self):
        return int(time.time())


if __name__ == '__main__':
    dateUtil = DateUtil()
    print dateUtil.getCurrentTime()
    print dateUtil.getCurrentTimeStamp()
