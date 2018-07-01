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
import threading

def_qr_path = '/work/ffstore_server/ffstore/static/qrcode/qrcode.png'
# def_qr_path = 'd:\\qrcode.png'
# def_qr_path = '/Users/ouyangfan/qrcode.png'


class WxBotUtil:
    def __init__(self, scan_qr_callback=None, qr_code_path=def_qr_path):
        self.logging = LogUtil().getLogging()
        self.qr_code_path = def_qr_path
        self.call_times = 0
        self.scan_qr_callback = scan_qr_callback

    def __call__(self, *args, **kwargs):
        self.login_by_thread()

    def login_callback(self):
        pass

    def qr_callback(self, **kwargs):
        uuid = kwargs['uuid']
        status = kwargs['status']
        qrcode = kwargs['qrcode']
        # self.logging.info("---> uuid: " + uuid)
        # self.logging.info("---> status: " + status)
        # self.logging.info("---> qrcode: " + qrcode)
        # print "---> uuid: ", uuid
        # print "---> status: ", status
        # print "---> qrcode: ", qrcode
        if self.call_times < 3:
            with open(self.qr_code_path, 'wb') as qr_file:
                qr_file.write(qrcode)
            NotifyAdmin().sendMsg(u'请网页扫码登陆运维微信', subject=SMS_SUBJECT_WX_LOGIN)
            self.call_times = self.call_times + 1
            if self.scan_qr_callback:
                self.scan_qr_callback(self.qr_code_path)

    def login_by_thread(self):
        thr = threading.Thread(target=self.login)
        thr.start()
        thr.join()

    def login(self):
        # remove the qr_code.png first
        if os.path.exists(self.qr_code_path):
            self.logging.info("---> remove qr code: " + str(self.qr_code_path))
            os.remove(self.qr_code_path)
        try:
            weichatListen = WeiChatListen(console_qr=True, qr_path=self.qr_code_path,
                                          qr_callback=self.qr_callback,
                                          login_callback=self.login_callback)
            # 启用puid
            weichatListen.bot.enable_puid('wxpy_puid.pkl')
            # my = weichatListen.bot.friends().search('asher')[0]
            # print weichatListen.bot.friends()
            my = weichatListen.bot.friends()[0]
            weichatListen.bot.self.add()
            weichatListen.bot.self.accept()
            weichatListen.listen(receivers=my)
            weichatListen.bot.join()
        except Exception as ex:
            self.logging.warn(ex)
            self.logging.warn("---> qr code exception: " + str(sys.exc_info()[0]))

if __name__ == '__main__':
    wxBot = WxBotUtil()
    wxBot.login_by_thread()
