#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/15
Desc:   订单类

_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
order_id VARCHAR(50) NOT NULL UNIQUE,
goods_id VARCHAR(50),
user_id VARCHAR(50),
order_goods_size VARCHAR(5),
order_goods_color VARCHAR(10),
order_status VARCHAR(10),
order_pay_time VARCHAR(20),
order_update_time VARCHAR(20),
order_express_num VARCHAR(50),
order_express_code VARCHAR(15),
foreign key (user_id) references ffstore_user(user_id) on delete cascade on update cascade
"""


class DbOrder:

    def __init__(self):
        self._order_id = None
        self._goods_id = None
        self._user_id = None
        self._order_goods_size = None
        self._order_goods_color = None
        self._order_goods_count = None
        self._order_status = None
        self._order_pay_time = None
        self._order_update_time = None
        self._order_express_num = None
        self._order_express_code = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def order_goods_size(self):
        return self._order_goods_size

    @order_goods_size.setter
    def order_goods_size(self, value):
        self._order_goods_size = value

    @property
    def order_goods_color(self):
        return self._order_goods_color

    @order_goods_color.setter
    def order_goods_color(self, value):
        self._order_goods_color = value

    @property
    def order_goods_count(self):
        return self._order_goods_count

    @order_goods_count.setter
    def order_goods_count(self, value):
        self._order_goods_count = value

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value

    @property
    def order_update_time(self):
        return self._order_update_time

    @order_update_time.setter
    def order_update_time(self, value):
        self._order_update_time = value

    @property
    def order_express_num(self):
        return self._order_express_num

    @order_express_num.setter
    def order_express_num(self, value):
        self._order_express_num = value

    @property
    def order_express_code(self):
        return self._order_express_code

    @order_express_code.setter
    def order_express_code(self, value):
        self._order_express_code = value
