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

import os
import sys
sys.path.append('../')

# windowds 得使用上面的
# from weichatutil.weichatutil.WeiChatListen import WeiChatListen
from weichatutil.WeiChatListen import WeiChatListen
from mgrsys.NotifyAdmin import NotifyAdmin, SMS_SUBJECT_WX_LOGIN
from util.LogUtil import LogUtil

def_qr_path = '/work/ffstore_server/ffstore/static/qrcode/qrcode.png'
# def_qr_path = 'd:\\qrcode.png'


class WxBotUtil:
    def __init__(self):
        self.logging = LogUtil().getLogging()
        pass

    def login_callback(self):
        pass

    def qr_callback(self, uuid, status, qrcode):
        self.logging.info("---> uuid: " + uuid)
        self.logging.info("---> status: " + status)
        self.logging.info("---> qrcode: " + qrcode)

    def login(self, qr_path=def_qr_path):
        # remove the qr_code.png first
        if os.path.exists(qr_path):
            self.logging.info("---> remove qr code: " + str(qr_path))
            os.remove(qr_path)
        weichatListen = None
        try:
            weichatListen = WeiChatListen(console_qr=True, qr_path=qr_path,
                                          login_callback=self.login_callback)
            my = weichatListen.bot.friends().search('ahser')[0]
            weichatListen.listen(receivers=my)
        except Exception as ex:
            self.logging.warn(ex)
            self.logging.warn("---> qr code exception: " + str(sys.exc_info()[0]))
        finally:
            NotifyAdmin().sendMsg(u'请网页扫码登陆运维微信', subject=SMS_SUBJECT_WX_LOGIN)
            weichatListen.bot.join()

if __name__ == '__main__':
    wxBot = WxBotUtil()
    wxBot.login()
