#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/7.
Desc:  微信消息回调接口
receive weiChat push msg
@see {#https://mp.weixin.qq.com/wxopen/devprofile?action=get_callback&token=1304670207&lang=zh_CN}
url: https://shmall.fansdroid.net/weichat/push/msg
Token: token20170907shmallweichatkey
EncodingAESKey: Cx4Nqorw8Gw7wWtIgPSoVbmLwJb20UnUkh36CKY0JPn
"""

import hashlib

token = 'token20170907shmallweichatkey'
EncodingAESKey = 'Cx4Nqorw8Gw7wWtIgPSoVbmLwJb20UnUkh36CKY0JPn'

class WeiChatMsg():
    def __init__(self, signature=None, timestamp=None, nonce=None):
        self.signature = signature
        self.timestamp = timestamp
        self.nonce = nonce

    def checkSignature(self):
        list = [token, self.timestamp, self.nonce]
        list.sort()     # sort
        str = "".join(list)   # list to string
        encryptStr = hashlib.sha1(str).hexdigest()
        print 'encryptStr = %s , signature = %s' %(encryptStr, self.signature)
        if self.signature == encryptStr:
            return True
        else:
            return False

