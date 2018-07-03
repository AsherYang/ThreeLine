#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/1
Desc:   用于发送微信消息

本类基于wxpy 以及 wechat_sender 同时结合自己weichatutil(私有pypi源) 进行搭建

注意：
1. 后台监听账号需要事先登录
2. 接受者，必须是后台监听的微信号的好友，才能成功发送消息

"""
import sys
sys.path.append('../')

import tornado.web
from mgrsys.NotifyAdmin import NotifyAdmin
from BaseResponse import BaseResponse
from constant import ResponseCode
from FFStoreJsonEncoder import *


class WxSendMsgHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        notify = NotifyAdmin()
        msg = self.get_argument('msg', default='test')
        receiver = self.get_argument('receiver', default='fan')
        notify.sendWxMsg(msg=msg, receiver=receiver)
        baseResponse = BaseResponse()
        baseResponse.code = ResponseCode.op_success
        baseResponse.desc = ResponseCode.op_success_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)

