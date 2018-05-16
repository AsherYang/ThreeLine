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

class User():

    @property
    def user_name(self):
        return self.user_name

    @property
    def user_name(self, value):
        self.user_name = value

    @property
    def user_tel(self):
        return self.user_tel

    @property
    def user_tel(self, value):
        self.user_tel = value

    @property
    def user_address(self):
        return self.user_address

    @property
    def user_address(self, value):
        self.user_address = value

    @property
    def buy_times(self):
        return self.buy_times

    @property
    def buy_times(self, value):
        self.buy_times = value

    @property
    def cost_count(self):
        return self.cost_count

    @property
    def cost_count(self, value):
        self.cost_count = value
