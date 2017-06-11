#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/6/11
Desc:   微信通知
"""

from wxpy import *
from wechat_sender import  *

bot = Bot('bot.pkl', console_qr=True)
bot.enable_puid()
master = ensure_one(bot.friends().search(puid='xxxx'))
log_group = ensure_one(bot.groups().search(puid='xxxxxx'))
other = ensure_one(bot.friends().search('xxxxxx'))
token = 'xxxxxxxxxxxxxxxxxxxxx'
listen(bot, [master, other, log_group], token=token, port=9090, status_report=True, status_receiver=log_group)