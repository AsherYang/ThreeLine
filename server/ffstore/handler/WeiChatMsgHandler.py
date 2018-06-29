#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : weichat msg forward tornado handler

用于接收到微信消息后，转发
"""
import sys
sys.path.append('../')
import tornado.web

from WeiChatMsg import WeiChatMsg
from util.SendMsgEmail import SendEmail
import threading


"""
receive weiChat push msg
@see {#https://mp.weixin.qq.com/wxopen/devprofile?action=get_callback&token=1304670207&lang=zh_CN}
url: https://shmall.fansdroid.net/weichat/push/msg
Token: token20170907shmallweichatkey
EncodingAESKey: Cx4Nqorw8Gw7wWtIgPSoVbmLwJb20UnUkh36CKY0JPn

https://ffstore.oyfstore.com/weichat/push/msg
Token:token20180625ffstoreweichatkey
EncodingAESKey:oJ48WmISVWaf2Xt91GnkchfRwct2FdLcE7sS7VoXJga
"""
class WeiChatMsgHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        print "signature = " + signature + " , timestamp = " + timestamp + " , nonce = " + nonce + " , echostr = " + echostr
        weiChatMsg = WeiChatMsg(signature, timestamp, nonce)
        if weiChatMsg.checkSignature():
            print 'ok. check success'
            self.write(echostr)
            self.sendEmail('FFStore有转发消息，请查看')
        else:
            print 'false. check fail'
            self.write('false. check fail')

    def post(self, *args, **kwargs):
        json_str = 'do not call post msg at weiChat msg'
        self.write(json_str)
        self.sendEmail('FFStore有转发消息，请查看')

    def sendEmail(self, msg):
        sendEmail = SendEmail()
        # sendEmail(content=msg)
        thr = threading.Thread(target=sendEmail, args=[msg])  # open new thread
        thr.start()
