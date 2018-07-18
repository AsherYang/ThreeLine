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
        param = json.loads(param)
        sign = param['sign']
        time = param['time']
        admin_tel = param['tel']
        sms_pwd = param['sms']
        cate_id = param['cateid']
        brand_id = param['brandid']
        goods_name = param['name']
        market_price = param['marketprice']
        current_price = param['currentprice']
        sale_count = param['salecount']
        stock_num = param['stocknum']
        status = param['status']
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
            if cate_id:
                dbGoods.cate_id = str(cate_id)
            if brand_id:
                dbGoods.brand_id = str(brand_id)
            if goods_name:
                dbGoods.goods_name = str(goods_name.encode('utf-8'))
            if market_price:
                dbGoods.market_price = str(market_price)
            if current_price:
                dbGoods.current_price = str(current_price)
            if sale_count:
                dbGoods.sale_count = str(sale_count)
            if stock_num:
                dbGoods.stock_num = str(stock_num)
            if status:
                dbGoods.status = str(status)
            else:
                dbGoods.status = str(GoodsStatus.STATUS_ON_SALE)
            if goods_code:
                dbGoods.goods_code = str(goods_code)
            if goods_logo:
                dbGoods.goods_logo = str(goods_logo)
            if thum_logo:
                dbGoods.thum_logo = str(thum_logo)
            if keywords:
                dbGoods.keywords = str(keywords.encode('utf-8'))
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


