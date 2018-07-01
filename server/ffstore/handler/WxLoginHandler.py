#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/1
Desc:   用于登录运维微信
   
本类基于wxpy 以及 wechat_sender 同时结合自己weichatutil(私有pypi源) 进行搭建

注意：
1. 后台监听账号需要事先登录
2. 接受者，必须是后台监听的微信号的好友，才能成功发送消息
"""

import sys
sys.path.append('../')

import tornado.web
from util.WxBotUtil import WxBotUtil, def_qr_path
from util.LogUtil import LogUtil


class WxLoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        wxBot = WxBotUtil(scan_qr_callback=self.scan_qr, qr_code_path=def_qr_path)
        wxBot.login_by_thread()
        # qr_path = 'qrcode/qrcode.png'
        # self.render('qrcode.html', qr_path=qr_path)

    def scan_qr(self, **kwargs):
        qr_path = kwargs['qr_path']
        logging = LogUtil().getLogging()
        logging.info('---> qrcPath: ' + qr_path)
        qr_path = 'qrcode/qrcode.png'
        self.render('qrcode.html', qr_path=qr_path)
