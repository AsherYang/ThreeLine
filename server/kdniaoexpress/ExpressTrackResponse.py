#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/14
Desc:   即时查询Api 返回结果对象实体
该对象实体，会在即时查询Api 返回中被设置为ExpressResponse#data字段中

字段直接拷贝自api文档，字段说明请参考：
http://www.kdniao.com/api-track
"""


class ExpressTrackResponse:
    def __init__(self):
        pass

    # 用户ID
    @property
    def EBusinessID(self):
        return self.EBusinessID

    @property
    def EBusinessID(self, value):
        self.EBusinessID = value

    # 订单编号
    @property
    def OrderCode(self):
        return self.OrderCode

    @property
    def OrderCode(self, value):
        self.OrderCode = value

    # 快递公司编码
    @property
    def ShipperCode(self):
        return self.ShipperCode

    @property
    def ShipperCode(self, value):
        self.ShipperCode = value

    # 物流运单号
    @property
    def LogisticCode(self):
        return self.LogisticCode

    @property
    def LogisticCode(self, value):
        self.LogisticCode = value

    # 成功与否
    @property
    def Success(self):
        return self.Success

    @property
    def Success(self, value):
        self.Success = value

    # 失败原因
    @property
    def Reason(self):
        return self.Reason

    @property
    def Reason(self, value):
        self.Reason = value

    # 物流状态：2-在途中,3-签收,4-问题件
    @property
    def State(self):
        return self.State

    @property
    def State(self, value):
        self.State = value

    # 快递轨迹
    @property
    def Traces(self):
        return self.Traces

    @property
    def Traces(self, value):
        self.Traces = value
