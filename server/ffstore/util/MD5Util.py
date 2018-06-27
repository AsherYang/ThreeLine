#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/25
Desc  : MD5 加密工具
"""

import hashlib
import hmac
import base64

# 微信小程序使用的API secret key
API_SECRET_KEY = 'md5.oyfstore.com'
# 后台管理系统使用的 Admin secret key
ADMIN_SECRET_KEY = 'admin.oyfstore.com'


class MD5Util:

    def __init__(self, value, secret_key=API_SECRET_KEY):
        self.value = value
        self.signValue = str(value) + secret_key
        self.signValue = self.signValue.encode('utf-8')
        # print 'signValue===> ', self.signValue

    def md5Signature(self):
        # print '------------signature-----------------'
        hashMd5 = hashlib.md5()
        hashMd5.update(self.signValue)
        # print hashMd5.hexdigest()
        return hashMd5.hexdigest()

    def hmacSignature(self):
        # print '------------hmacSign-----------------'
        print hmac.new(self.signValue).hexdigest()
        print hmac.new(API_SECRET_KEY, str(self.value)).hexdigest()

    def base64Signature(self):
        # print '---------------base64--------------'
        print base64.b16encode(self.signValue)
        print base64.b32encode(self.signValue)
        print base64.b64encode(self.signValue)

    def shaSignature(self):
        # print '---------------shaSign--------------'
        print hashlib.sha1(self.signValue).hexdigest()
        print hashlib.sha224(self.signValue).hexdigest()
        print hashlib.sha256(self.signValue).hexdigest()
        print hashlib.sha384(self.signValue).hexdigest()
        print hashlib.sha512(self.signValue).hexdigest()


if __name__ == '__main__':
    md5Util = MD5Util(20180625193325)
    md5Util.md5Signature()
    md5Util.hmacSignature()
    md5Util.base64Signature()
    md5Util.shaSignature()
