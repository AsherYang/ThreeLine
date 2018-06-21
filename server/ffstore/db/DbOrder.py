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
        pass

    @property
    def order_id(self):
        return self.order_id

    @property
    def order_id(self, value):
        self.order_id = value

    @property
    def goods_id(self):
        return self.goods_id

    @property
    def goods_id(self, value):
        self.goods_id = value

    @property
    def user_id(self):
        return self.user_id

    @property
    def user_id(self, value):
        self.user_id = value

    @property
    def order_goods_size(self):
        return self.order_goods_size

    @property
    def order_goods_size(self, value):
        self.order_goods_size = value

    @property
    def order_goods_color(self):
        return self.order_goods_color

    @property
    def order_goods_color(self, value):
        self.order_goods_color = value

    @property
    def order_goods_count(self):
        return self.order_goods_count

    @property
    def order_goods_count(self, value):
        self.order_goods_count = value

    @property
    def order_status(self):
        return self.order_status

    @property
    def order_status(self, value):
        self.order_status = value

    @property
    def order_pay_time(self):
        return self.order_pay_time

    @property
    def order_pay_time(self, value):
        self.order_pay_time = value

    @property
    def order_update_time(self):
        return self.order_update_time

    @property
    def order_update_time(self, value):
        self.order_update_time = value

    @property
    def order_express_num(self):
        return self.order_express_num

    @property
    def order_express_num(self, value):
        self.order_express_num = value

    @property
    def order_express_code(self):
        return self.order_express_code

    @property
    def order_express_code(self, value):
        self.order_express_code = value