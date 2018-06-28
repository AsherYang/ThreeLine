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

    def __init__(self, secret_key=API_SECRET_KEY):
        self.secret_key = secret_key

    def md5Signature(self, value):
        # print '------------signature-----------------'
        signValue = str(value) + self.secret_key
        signValue = signValue.encode('utf-8')
        hashMd5 = hashlib.md5()
        hashMd5.update(signValue)
        # print hashMd5.hexdigest()
        return hashMd5.hexdigest()

    def hmacSignature(self, value):
        # print '------------hmacSign-----------------'
        signValue = str(value) + self.secret_key
        signValue = signValue.encode('utf-8')
        print hmac.new(signValue).hexdigest()
        print hmac.new(self.secret_key, str(value)).hexdigest()

    def base64Signature(self, value):
        # print '---------------base64--------------'
        signValue = str(value) + self.secret_key
        signValue = signValue.encode('utf-8')
        print base64.b16encode(signValue)
        print base64.b32encode(signValue)
        print base64.b64encode(signValue)

    def shaSignature(self, value):
        # print '---------------shaSign--------------'
        signValue = str(value) + self.secret_key
        signValue = signValue.encode('utf-8')
        print hashlib.sha1(signValue).hexdigest()
        print hashlib.sha224(signValue).hexdigest()
        print hashlib.sha256(signValue).hexdigest()
        print hashlib.sha384(signValue).hexdigest()
        print hashlib.sha512(signValue).hexdigest()


if __name__ == '__main__':
    md5Util = MD5Util()
    md5Util.md5Signature(20180625193325)
    md5Util.hmacSignature(20180625193325)
    md5Util.base64Signature(20180625193325)
    md5Util.shaSignature(20180625193325)
