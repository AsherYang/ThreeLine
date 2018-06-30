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

    """
    参考: doc [http://wxpy.readthedocs.io/zh/latest/_modules/wxpy/api/bot.html]
    :param cache_path:
            * 设置当前会话的缓存路径，并开启缓存功能；为 `None` (默认) 则不开启缓存功能。
            * 开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
            * 设为 `True` 时，使用默认的缓存路径 'wxpy.pkl'。
    :param console_qr:
        * 在终端中显示登陆二维码，需要安装 pillow 模块 (`pip3 install pillow`)。
        * 可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 `True` 时，也将在内部当作 2)。
        * 也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
        * 例如: 在大部分 Linux 系统中可设为 `True` 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
    :param qr_path: 保存二维码的路径
    :param qr_callback: 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
    :param login_callback: 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
    :param logout_callback: 登出时的回调

    windows 下终端输出可以选择 console_qr=1，或者选择已文件形式输出:console_qr=False, qr_path='d:\\qr_code.png'
    linux 下由于python27会报 `global name 'FileNotFoundError' is not defined`, 所以选择console_qr=True。(注意选择1 会导致终端输出不正确)
    """
    def __init__(self, console_qr=True, qr_path=None, qr_callback=None, login_callback=None, logout_callback=None):
        self.bot = Bot('bot.pkl', console_qr=console_qr, qr_path=qr_path, qr_callback=qr_callback,
                       login_callback=login_callback, logout_callback=logout_callback)
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
    weichatListen = WeiChatListen(console_qr=1, qr_path='d:\\qr_code.png')
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
