#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/15
Desc:   订单数据库操作类

只要是操作类订单数据类，该订单的更新时间order_update_time 必须为最新时间，
便于查询处理
"""

from DbOrder import DbOrder
from ffstore.constant import OrderStatus
from ffstore.util import DbUtil
from ffstore.util.DateUtil import DateUtil

class OrderDao:

    def __init__(self):
        self.dateUtil = DateUtil()
        pass

    # 创建订单
    def saveToDb(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            currentTime = self.dateUtil.getCurrentTime()
            insert = 'insert into ffstore_order (order_id, goods_id, user_id, order_goods_size, order_goods_color,' \
                     ' order_status, order_pay_time, order_update_time, order_express_num, order_express_code)' \
                     ' values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' \
                     % (orderInfo.order_id, orderInfo.goods_id, orderInfo.user_id, orderInfo.order_goods_size,
                        orderInfo.order_goods_color, orderInfo.order_status, orderInfo.order_pay_time,
                        currentTime, orderInfo.order_express_num, orderInfo.order_express_code)
            print 'insert order to db.'
            return DbUtil.insert(insert)
        return False

    # 根据订单ID，更新订单所有信息，会更新所有订单表字段，如果需要更新单个字段值，请使用单个更新的方式
    def updateToDb(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            currentTime = self.dateUtil.getCurrentTime()
            update = 'update ffstore_order set goods_id = "%s", user_id = "%s", order_goods_size = "%s",' \
                     ' order_goods_color = "%s", order_status = "%s", order_pay_time = "%s", order_update_time = "%s", ' \
                     'order_express_num = "%s", order_express_code = "%s" where order_id = "%s" ' \
                     % (orderInfo.goods_id, orderInfo.user_id, orderInfo.order_goods_size, orderInfo.order_goods_color,
                        orderInfo.order_status, orderInfo.order_pay_time, currentTime, orderInfo.order_express_num,
                        orderInfo.order_express_code, orderInfo.order_id)
            print 'update order information to db'
            return DbUtil.update(update)
        return False

    # 下订单，更新订单, 为了保证下订单时数据正确性，需要将所有数据全部更新为当前下订单时的最新数据信息。
    # 根据订单ID，下订单时，更新订单，此时需要将订单状态status 改为"待发货"状态, 并且更新订单下单时间
    def updateByPayment(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            orderInfo.order_pay_time = self.dateUtil.getCurrentTime()
            orderInfo.order_status = OrderStatus.STATUS_NO_DELIVERY
            return self.updateToDb(orderInfo)
        return False

    # 根据订单ID，更新订单快递信息
    # 用于增加快递单信息，此时需要将订单状态status 改为"待收货"状态
    def updateExpress(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            currentTime = self.dateUtil.getCurrentTime()
            orderInfo.order_status = OrderStatus.STATUS_NO_RECEIVE
            update = 'update ffstore_order set order_status = "%s", order_update_time = "%s", ' \
                     'order_express_num = "%s", order_express_code = "%s" where order_id = "%s" ' \
                     % (orderInfo.order_status, currentTime, orderInfo.order_express_num,
                        orderInfo.order_express_code, orderInfo.order_id)
            return DbUtil.update(update)
        return False

    # 订单完成
    # 根据订单ID，订单完成时，更新订单，此时需要将订单状态status 改为"订单完成"状态
    def updateByCompleted(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            orderInfo.order_status = OrderStatus.STATUS_COMPLETE
            return self.updateStatus(orderInfo)
        return False

    # 根据订单ID，更新订单状态{@see #OrderStatus}
    def updateStatus(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            currentTime = self.dateUtil.getCurrentTime()
            update = 'update ffstore_order set order_status = "%s", order_update_time = "%s" where order_id = "%s" ' \
                     % (orderInfo.order_status, currentTime, orderInfo.order_id)
            return DbUtil.update(update)
        return False

    # 根据订单ID 以及商品ID，更新订单商品信息(尺码和颜色)
    def updateGoodsSizeAndColor(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            currentTime = self.dateUtil.getCurrentTime()
            update = 'update ffstore_order set order_goods_size = "%s", order_goods_color = "%s", ' \
                     'order_update_time = "%s" where order_id = "%s" and goods_id = "%s" ' \
                     % (orderInfo.order_goods_size, orderInfo.order_goods_color, currentTime, orderInfo.order_id,
                        orderInfo.goods_id)
            return DbUtil.update(update)
        return False

    # 根据订单ID，查询单个订单
    def queryByOrderId(self, order_id):
        if not order_id:
            return None
        query = 'select * from ffstore_order where order_id = "%s" ' % order_id
        return DbUtil.query(query)

    # 根据用户ID，查询单个用户所有订单
    def queryByUserId(self, user_id):
        if not user_id:
            return None
        query = 'select * from ffstore_order where user_id = "%s" ' % user_id
        return DbUtil.query(query)

    # 根据商品ID，查询该商品对应的所有用户订单
    def queryByGoodsId(self, goods_id):
        if not goods_id:
            return None
        query = 'select * from ffstore_order where goods_id = "%s" ' % goods_id
        return DbUtil.query(query)

    # 根据商品ID 以及订单状态，查询该商品对应改状态下，所有用户的订单
    def queryByGoodsIdAndStatus(self, goods_id, order_status):
        if not goods_id or not order_status:
            return None
        query = 'select * from ffstore_order where goods_id = "%s" and order_status= "%s" ' % (goods_id, order_status)
        return DbUtil.query(query)

    # 根据用户ID 和订单状态，查询该用户对应状态的所有订单
    def queryByUserIdAndStatus(self, user_id, order_status, page_num=1, page_size=10):
        if not user_id or not order_status:
            return None
        start = (page_num - 1) * page_size
        # query = 'select * from ffstore_order where user_id = "%s" and order_status= "%s" ' % (user_id, order_status)
        query = 'select * from ffstore_order where user_id = "%s" and order_status= "%s" limit %s, %s; ' \
                % (user_id, order_status, start, page_size)
        return DbUtil.query(query)

    # 根据订单状态，查询所有用户对应该状态的订单
    def queryByStatus(self, order_status):
        if not order_status:
            return None
        query = 'select * from ffstore_order where order_status= "%s" ' % (order_status)
        return DbUtil.query(query)

    # 查询这段时间内下单的所有用户的订单， 查询的订单结果，会包含其他状态的订单
    def queryByPayTimeInterval(self, start_time, end_time):
        if not start_time or not end_time:
            return None
        query = 'select * from ffstore_order where order_pay_time >= UNIX_TIMESTAMP("%s") and ' \
                'order_pay_time < UNIX_TIMESTAMP("%s")' % (start_time, end_time)
        return DbUtil.query(query)

    # 查询这段时间内更新订单的所有用户的订单， 查询的订单结果，会包含其他状态的订单
    def queryByUpdateTimeInterval(self, start_time, end_time):
        if not start_time or not end_time:
            return None
        query = 'select * from ffstore_order where order_update_time >= UNIX_TIMESTAMP("%s") and ' \
                'order_pay_time < UNIX_TIMESTAMP("%s")' % (start_time, end_time)
        return DbUtil.query(query)

    # 根据用户ID，查询单个用户的订单总量
    def queryCountByUserId(self, user_id):
        if not user_id:
            return 0
        query = 'select count(*) from ffstore_order where user_id = "%s" ' % user_id
        return DbUtil.query(query)

    # 根据商品ID，查询该商品对应的订单总量
    def queryCountByGoodsId(self, goods_id):
        if not goods_id:
            return 0
        query = 'select count(*) from ffstore_order where goods_id = "%s" ' % goods_id
        return DbUtil.query(query)

    # 查询这段时间内订单的总量
    def queryCountByPayTimeInterval(self, start_time, end_time):
        if not start_time or not end_time:
            return 0
        query = 'select count(*) from ffstore_order where order_update_time >= UNIX_TIMESTAMP("%s") and ' \
                'order_pay_time < UNIX_TIMESTAMP("%s")' % (start_time, end_time)
        return DbUtil.query(query)

    # 删除单个订单，当用户添加订单后，取消订单，此时需要删除该订单
    # 只有当订单状态为"未支付" 状态下，才允许删除订单，其他状态不允许进行删除操作
    def deleteByOrderId(self, orderInfo):
        if isinstance(orderInfo, DbOrder):
            if orderInfo.order_status == OrderStatus.STATUS_NO_PAYMENT:
                delete = 'delete from ffstore_order where order_id = "%s" and order_status = "%s" ' \
                         % (orderInfo.order_id, OrderStatus.STATUS_NO_PAYMENT)
                print 'delete order_id:%s from db.' % orderInfo.order_id
                return DbUtil.delete(delete)
            return False
        return False
