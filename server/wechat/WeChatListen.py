#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/6/11
Desc:   微信通知
"""

from wxpy import *
from wechat_sender import *


token = 'd9218b046dde43147ea6c889ea67ede8437ff696'
port = '9091'

bot = Bot('bot.pkl', console_qr=True)
bot.enable_puid()

# for friend in bot.friends():
#     print friend.puid, friend.name

asher = ensure_one(bot.friends().search(puid='6e7c1b59'))
fan = ensure_one(bot.friends().search(puid='755575b7'))
fen = ensure_one(bot.friends().search(puid='6ebf1db1'))
fei = ensure_one(bot.friends().search(puid='13dbc656'))
# log_group = ensure_one(bot.groups().search(puid='xxxxxx'))

listen(bot, receivers=[fan, fen], token=token, port=port, status_report=True, status_receiver='asher')
