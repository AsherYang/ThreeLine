#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/29
Desc:  通知类   
"""

from util.SendMsgEmail import SendEmail
import threading
from weichatutil.WeiChatSender import WeiChatSender

# 发送短信验证码给当前管理员
SMS_SUBJECT_PWD = u'短信验证码'
# 发送登录信息给超级管理员(我)
SMS_SUBJECT_LOGIN = u'系统登录'


class NotifyAdmin:
    def __init__(self):
        pass

    """
    发送短信通知
    """
    def sendMsg(self, sms_msg, toaddrs=['13553831061@139.com'], subject='ffstore'):
        sendEmail = SendEmail(toaddrs, subject)
        thr = threading.Thread(target=sendEmail, args=[sms_msg])  # open new thread
        thr.start()

    """
    发送微信通知
    """
    def sendWxMsg(self, msg, receiver='Fan'):
        wxSender = WeiChatSender()
        wxSender.sendMsg(msg, receiver=receiver)
        pass
