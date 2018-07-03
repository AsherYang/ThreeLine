#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/29
Desc:  通知类   
"""

import sys
sys.path.append('../')

from util.SendMsgEmail import SendEmail
import threading
# windowds 得使用上面的
# from weichatutil.weichatutil.WeiChatSender import WeiChatSender
from weichatutil.WeiChatSender import WeiChatSender
from util.DateUtil import DateUtil

# 发送短信验证码给当前管理员
SMS_SUBJECT_PWD = u'短信验证码'
# 发送登录信息给超级管理员(我)
SMS_SUBJECT_LOGIN = u'系统登录'
# 发送非法客户端登陆信息给超级管理员(我)
SMS_SUBJECT_INVALID_ADMIN_LOGIN = u'!! 非法客户端登陆 !!'
# 运维报警微信登录
SMS_SUBJECT_WX_LOGIN = u'运维微信登录'


class NotifyAdmin:
    def __init__(self):
        pass

    """
    发送短信通知
    """
    def sendMsg(self, sms_msg, toaddrs=['13553831061@139.com'], subject='ffstore'):
        sendEmail = SendEmail(toaddrs=toaddrs, subject=subject)
        thr = threading.Thread(target=sendEmail, args=[sms_msg])  # open new thread
        thr.start()

    """
    发送微信通知
    """
    def sendWxMsg(self, msg, receiver='Fan'):
        weichatSender = WeiChatSender(host='http://127.0.0.1', port='9091')
        weichatSender.sendMsg(msg, receiver=receiver)
        pass

if __name__ == '__main__':
    notify = NotifyAdmin()
    current_time = DateUtil().getCurrentTime()
    notify.sendWxMsg('Hello. oyf finish it. at: %s' % current_time)
    notify.sendMsg('456')
