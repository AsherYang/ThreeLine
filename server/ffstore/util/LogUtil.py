#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/23
Desc  : log 输出工具，用于在linux 终端输出到指定文件
"""

import logging

default_log_file = '/work/ffstore_server/logs/ffstore.log'


class LogUtil:

    """
    init log util
    """

    def __init__(self, logFileName=default_log_file):
        pass
        # logging.basicConfig(
        #     level=logging.DEBUG,
        #     format='%(asctime)s-%(levelname)s-%(message)s',
        #     datefmt='%y-%m-%d %H:%M',
        #     filename=logFileName,
        #     filemode='w'
        # )
        # console = logging.StreamHandler()
        # console.setLevel(logging.INFO)
        # formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        # console.setFormatter(formatter)
        # logging.getLogger('').addHandler(console)

    def getLogging(self):
        return logging
