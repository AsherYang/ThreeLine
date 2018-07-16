#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   用户类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
user_name VARCHAR(50),
user_tel VARCHAR(20) NOT NULL UNIQUE,
user_address VARCHAR(512),
buy_times INT,
cost_count INT
"""


class DbUser:

    def __init__(self):
        self._user_id = None
        self._user_name = None
        self._user_tel = None
        self._user_address = None
        self._buy_times = None
        self._cost_count = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    @property
    def user_tel(self):
        return self._user_tel

    @user_tel.setter
    def user_tel(self, value):
        self._user_tel = value

    @property
    def user_address(self):
        return self._user_address

    @user_address.setter
    def user_address(self, value):
        self._user_address = value

    @property
    def buy_times(self):
        return self._buy_times

    @buy_times.setter
    def buy_times(self, value):
        self._buy_times = value

    @property
    def cost_count(self):
        return self._cost_count

    @cost_count.setter
    def cost_count(self, value):
        self._cost_count = value
