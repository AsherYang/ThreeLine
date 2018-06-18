#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/16
Desc  : 获取订单接口. 返回网络数据

https://sujiefs.com//api/mall/goodsOrder/getMyOrderList?openId=oeuj50KHMqsh5kYZYWQJuwmY5yG0&orderStatus=0&receiveFlg=0&page=1&size=10&type=1&sign=c1cc2cc92f2553ab382d612bb6c379b2&time=20180611214443
1. 小程序请求的order 都是针对单个用户的订单情况
2. 后台程序请求的order 可以是多个用户的订单情况
"""
from ffstore.db.UserDao import UserDao
from ffstore.db.DbUser import DbUser
from ffstore.db.OrderDao import OrderDao
from ffstore.db.DbOrder import DbOrder

class GetOrder:
    def __init__(self):
        self.userDao = UserDao()
        self.orderDao = OrderDao()

    """
    小程序, 获取单个用户的订单接口
    user_id: 用户ID信息
    order_status:订单状态{@see #OrderStatus}
    receive_flag:收货状态(暂不支持，接口中已去除，根据order_status处理)
    type: 1:全部订单;  2:补货订单(暂不支持，接口中已去除)
    page_num: 分页页码
    page_size: 分页每页数量
    """
    def getMyOrderList(self, user_id, order_status, page_num=1, page_size=10):
        if not user_id:
            return None
        user = self.userDao.queryByUserId(user_id)
        if not user:
            return None
        dbOrderList = self.orderDao.queryByUserIdAndStatus(user, order_status)
        pass

    """
    小程序, 获取单个用户的的订单总数
    
    """
    def getMyOrderSize(self):
        pass
