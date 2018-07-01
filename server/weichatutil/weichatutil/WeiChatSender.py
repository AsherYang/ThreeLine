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

def_host = 'http://127.0.0.1'
# 是使用Token.py 随意生成的，但是要保证Listen和sender一致
def_token = 'd9218b046dde43147ea6c889ea67ede8437ff696'
def_port = '9091'


class WeiChatSender:

    def __init__(self, token=def_token, host=def_host, port=def_port):
        self.token = token
        self.host = host
        self.port = port

    def sendMsg(self, msg, receiver='fan'):
        sender = Sender(token=self.token, host=self.host, port=self.port)
        # sender.send('HELLO ASHER345')
        sender.send_to(msg, receiver)

if __name__ == '__main__':
    weichatSender = WeiChatSender(host='http://127.0.0.1', port='9091')
    weichatSender.sendMsg('hello oyf. what a nice day')
