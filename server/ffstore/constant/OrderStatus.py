#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/13
Desc  : 订单状态
"""

# 待支付
STATUS_NO_PAYMENT = 1
# 待发货(已支付)
STATUS_NO_DELIVERY = 2
# 待收货(已发货, 快递中)
STATUS_NO_RECEIVE = 3
# 退款中(已申请退款)
STATUS_NEED_REFUND = 4
# 退款完成
STATUS_COMPLETE_REFUND = 5
# 订单完成(已收货)
STATUS_COMPLETE = 10
