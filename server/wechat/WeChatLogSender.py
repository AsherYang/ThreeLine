#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/6/11
Desc:   微信通知
"""

from wechat_sender import *
import logging

# WechatSender().send('Hello AsherYang')
# Sender().send_to('hello msg', '芬')

logger = logging.getLogger(__name__)
def init_logger():
    sender_logger = LoggingSenderHandler('threeline', level=logging.ERROR)
    logger.addHandler(sender_logger)

def test_log_sender():
    logger.exception('exception: what fuck.')

if __name__ == '__main__':
    init_logger()
    test_log_sender()
    Sender().send_to('hello Fen', '芬')
    Sender('小逗比').send('hello')