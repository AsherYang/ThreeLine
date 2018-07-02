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
from tornado.web import asynchronous
from BaseResponse import BaseResponse
from constant import ResponseCode
from FFStoreJsonEncoder import *

from util.WxBotUtil import WxBotUtil, def_qr_path
from util.LogUtil import LogUtil
import threading
import os


class WxLoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        wxBot = WxBotUtil()
        # wxBot.login_by_thread()
        thr = threading.Thread(target=wxBot)  # open new thread,  args=[sms_msg], thread move to WxBotUtil
        thr.start()
        qr_path = '../static/qrcode/qrcode.png'
        self.redirect(qr_path)

        # self.render('qrcode.html', qr_path=qr_path)
        # self.scan_qr(qr_path='/work/ffstore_server/ffstore/static/qrcode/qrcode.png')

    # 因为WxBotUtil中 bot 是线程阻塞类型，所以回调回来会出现问题, 直接redirect 到二维码静态页面
    # def scan_qr(self, **kwargs):
    #     qr_path = str(kwargs['qr_path'])
    #     logging = LogUtil().getLogging()
    #     logging.info('---> qrcPath: ' + qr_path)
    #     logging.info('--------------------------------------')
    #     # qr_path = '/work/ffstore_server/ffstore/static/qrcode/qrcode.png'
    #     if os.path.exists(qr_path) and qr_path.find('static') != -1:
    #         qr_code_path = qr_path[qr_path.find('static')+7:]
    #         logging.info('---> do qrcPath: ' + qr_code_path)
    #         logging.info('-----------------111111111---------------------')
    #         # self.render('1111111111111111111111')
    #         # return self.render('qrcode.html', qr_path=qr_code_path)
    #     #     # qr_path = 'qrcode/qrcode.png'
    #     else:
    #         baseResponse = BaseResponse()
    #         baseResponse.code = ResponseCode.fail_wx_bot_login
    #         baseResponse.desc = ResponseCode.fail_wx_bot_login_desc
    #         json_str = json.dumps(baseResponse, cls=StrEncoder)
    #         self.write(json_str)
    #     self.finish()
