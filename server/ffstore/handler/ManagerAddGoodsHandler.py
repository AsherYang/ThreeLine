#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/5
Desc  : 后台管理系统， 添加商品handler

manager api handler

"""

import sys
sys.path.append('../')
import tornado.web
from constant import ResponseCode
from FFStoreJsonEncoder import *

from mgrsys.PermissionManager import PermissionManager
from util.GenerateIDUtil import GenerateIDUtil
from net.GetGoods import GetGoods
from db.DbGoods import DbGoods
from constant import GoodsStatus


class ManagerAddGoodsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        prarm = json.loads(param)
        sign = prarm['sign']
        time = prarm['time']
        admin_tel = prarm['tel']
        sms_pwd = prarm['sms']
        cate_id = param['cateid']
        brand_id = param['brandid']
        goods_name = param['name']
        market_price = param['marketprice']
        current_price = param['currentprice']
        sale_count = param['salecount']
        stock_num = param['stocknum']
        goods_code = param['goodscode']
        goods_logo = param['goodslogo']
        thum_logo = param['thumlogo']
        keywords = param['keywords']

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            genIdUtil = GenerateIDUtil()
            dbGoods = DbGoods()
            dbGoods.goods_id = genIdUtil.getUID()
            dbGoods.cate_id = cate_id
            dbGoods.brand_id = brand_id
            dbGoods.goods_name = goods_name
            dbGoods.market_price = market_price
            dbGoods.current_price = current_price
            dbGoods.sale_count = sale_count
            dbGoods.stock_num = stock_num
            dbGoods.status = GoodsStatus.STATUS_ON_SALE
            dbGoods.goods_code = goods_code
            dbGoods.goods_logo = goods_logo
            dbGoods.thum_logo = thum_logo
            dbGoods.keywords = keywords
            getGoods = GetGoods()
            saveResult = getGoods.saveOrUpdateToDb(goods=dbGoods)
            if saveResult:
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.code = ResponseCode.fail_op_db_data
                baseResponse.desc = ResponseCode.fail_op_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)


