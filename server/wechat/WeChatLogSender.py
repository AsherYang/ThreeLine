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
host = 'http://www.fansdroid.net'
token = 'd9218b046dde43147ea6c889ea67ede8437ff696'
port = '9091'

def init_logger():
    sender_logger = LoggingSenderHandler('threeline', level=logging.ERROR)
    logger.addHandler(sender_logger)

def test_log_sender():
    logger.exception('exception: what fuck.')

if __name__ == '__main__':
    # init_logger()
    # test_log_sender()
    # sender = Sender(token=token, receiver='fen', host=host, port=port)
    sender = Sender(token=token, host=host, port=port)
    # sender.send('HELLO ASHER345')
    sender.send_to('hello asher', 'fen')
