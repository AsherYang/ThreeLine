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
import logging

def_token = 'd9218b046dde43147ea6c889ea67ede8437ff696'
def_port = '9091'

# bot = Bot('bot.pkl', console_qr=1)
# bot.enable_puid()

# for friend in bot.friends():
#     print friend.puid, friend.name

# asher = ensure_one(bot.friends().search(puid='6e7c1b59'))
# fan = ensure_one(bot.friends().search(puid='755575b7'))
# fen = ensure_one(bot.friends().search(puid='6ebf1db1'))
# fei = ensure_one(bot.friends().search(puid='13dbc656'))
# log_group = ensure_one(bot.groups().search(puid='xxxxxx'))

class WeiChatListen:

    def __init__(self, console_qr=1):
        self.bot = Bot('bot.pkl', console_qr=console_qr)
        self.bot.enable_puid()
        self.logger = logging.getLogger(__name__)

    def getFriendByPuid(self, puid):
        return ensure_one(self.bot.friends().search(puid=puid))

    def getFriendByName(self, name):
        return self.bot.friends().search(name)[0]

    def getAllFriends(self):
        return self.bot.friends()

    def init_logger(self):
        sender_logger = LoggingSenderHandler('ffstore', level=logging.WARN)
        self.logger.addHandler(sender_logger)

    def listen(self, receivers=None, token=def_token, port=def_port):
        listen(self.bot, receivers=receivers, token=token, port=port, status_report=True, status_receiver='asher')

if __name__ == '__main__':
    weichatListen = WeiChatListen(0)
    # print weichatListen.getAllFriends()
    # print '>>>>>>>>>>>'
    # print weichatListen.bot.friends()
    # for friend in weichatListen.bot.friends():
    #     print '--------'
    #     print friend.puid
    #     print friend.name
    my = weichatListen.bot.friends().search('ahser')[0]
    # my2 = weichatListen.getFriendByName('asher')
    weichatListen.listen(receivers=my)
