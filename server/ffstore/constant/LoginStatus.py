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
# 登录未找到对应用户(管理员), 用户名|密码不正确,请重新登录
STATUS_LOGIN_NO_ADMIN = 2
# 登录时效过期
STATUS_LOGIN_OUT_OF_DATE = 3
