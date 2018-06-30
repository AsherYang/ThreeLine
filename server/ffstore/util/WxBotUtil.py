#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/30
Desc  : wxpy 在linux 下，登陆，以及进行监听的工具类
该工具类主要是用来解决wxpy 在linux 下登陆遇到的问题
将二维码输出到文件中， 然后通过浏览器访问二维码进行登陆

1. 该工具引用 https://pypi.ffstore.com/simple 下的 weichatutil 工具
2. weichatutil封装 https://github.com/bluedazzle/wechat_sender 以及封装 https://github.com/youfou/wxpy

https://www.kancloud.cn/wizardforcel/tornado-overview/141667
"""

from weichatutil.WeiChatListen import WeiChatListen
from mgrsys.NotifyAdmin import NotifyAdmin, SMS_SUBJECT_WX_LOGIN
import os


def_qr_path = '/work/ffstore_server/images/qrcode/qr_code.png'


class WxBotUtil:
    def __init__(self):
        pass

    def login(self, qr_path=def_qr_path):
        try:
            # remove the qr_code.png first
            if os.path.exists(qr_path):
                os.remove(qr_path)
            weichatListen = WeiChatListen(console_qr=False, qr_path=qr_path)
            my = weichatListen.bot.friends().search('ahser')[0]
            weichatListen.listen(receivers=my)
            NotifyAdmin.sendMsg(u'请登录网页扫码登陆运维微信', subject=SMS_SUBJECT_WX_LOGIN)
        except:
            pass
