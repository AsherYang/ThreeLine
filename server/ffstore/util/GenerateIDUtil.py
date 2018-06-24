#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/24
Desc:   分布式ID生成器

使用 pysnowflake
参考资料: https://www.cnblogs.com/galengao/p/5780519.html
有道云笔记: python pysnowflake 生成唯一id
"""

import snowflake.client

host = '127.0.0.1'
port = 58001


class GenerateIDUtil:
    def __init__(self):
        snowflake.client.setup(host, port)

    def getUID(self):
        return snowflake.client.get_guid()

    def getStatus(self):
        return snowflake.client.get_stats()
