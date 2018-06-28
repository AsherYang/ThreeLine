#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/27
Desc:   (管理员)登录状态
"""

# 登录成功
STATUS_LOGIN_SUCCESS = 1
# 登录未找到对应用户(管理员), 管理员号码不存在, 非法操作
STATUS_LOGIN_NO_ADMIN = 2
# 登录短信验证码错误, 一般这种情况，说明手机号码存在，但是验证码错误，需要重新发送验证码给管理员(登录时)
STATUS_LOGIN_FAIL_PWD = 3
# 登录时效过期
STATUS_LOGIN_OUT_OF_DATE = 4
