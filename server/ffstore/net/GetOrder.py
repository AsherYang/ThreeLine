#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/16
Desc  : 获取订单接口. 返回网络数据

1. 小程序请求的order 都是针对单个用户的订单情况
2. 后台程序请求的order 可以是多个用户的订单情况
"""
from ffstore.db.UserDao import UserDao
from ffstore.db.DbUser import DbUser
from ffstore.db.OrderDao import OrderDao
from ffstore.db.DbOrder import DbOrder
from ffstore.db.GoodsDao import GoodsDao
from ffstore.net.GetGoods import GetGoods

class GetOrder:
    def __init__(self):
        self.userDao = UserDao()
        self.orderDao = OrderDao()
        self.goodsDao = GoodsDao()
        self.getGoods = GetGoods()

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
        dbOrderResult = self.orderDao.queryByUserIdAndStatus(user, order_status, page_num, page_size)
        dbOrderList = self.convertDbRow2OrderList(dbOrderResult)
        if not dbOrderList:
            return None
        goodsIdList = []
        for order in dbOrderList:
            goodsIdList.append(order.order_id)
        if not goodsIdList:
            return None
        dbGoodsList = self.getGoods.getDbGoodsByIdList(goodsIdList)
        # todo
        # return convert2NetOrder()
        pass

    """
    小程序, 获取单个用户的的订单总数
    """
    def getMyOrderSize(self, user_id):
        if not user_id:
            return 0
        return self.orderDao.queryCountByUserId(user_id)

    """
    小程序，获取单个用户的，特定订单状态的订单总数
    """
    def getMyOrderStatusSize(self, user_id, order_status):
        if not user_id:
            return 0
        return self.orderDao.queryCountByUserIdAndStatus(user_id, order_status)

    # 将数据库查询出来的结果，对应设置给category实体bean, 并作为集合返回出去
    def convertDbRow2OrderList(self, dbOrderAllRowsResult):
        if not dbOrderAllRowsResult:
            return None
        orderList = []
        for row in dbOrderAllRowsResult:
            dbOrder = DbOrder()
            row_id = row[0]
            dbOrder.order_id = row[1]
            dbOrder.goods_id = row[2]
            dbOrder.user_id = row[3]
            dbOrder.order_goods_size = row[4]
            dbOrder.order_goods_color = row[5]
            dbOrder.order_goods_count = row[6]
            dbOrder.order_status = row[7]
            dbOrder.order_pay_time = row[8]
            dbOrder.order_update_time = row[9]
            dbOrder.order_express_num = row[10]
            dbOrder.order_express_code = row[11]
            orderList.append(dbOrder)
        return orderList
