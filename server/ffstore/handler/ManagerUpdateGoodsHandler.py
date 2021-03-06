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
from net.GetGoods import GetGoods
from net.GetGoodsPhoto import GetGoodsPhoto
from net.GetGoodsAttr import GetGoodsAttr
from db.DbGoods import DbGoods
from db.DbGoodsPhoto import DbGoodsPhoto
from db.DbAttribute import DbAttribute


class ManagerUpdateGoodsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        sign = param['sign']
        time = param['time']
        admin_tel = param['tel']
        sms_pwd = param['sms']
        goods_id = param['goodsid']
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

        # goods picture
        photo_thum_list = param['photosthumlist']

        # goods attribute
        attr_market_year = param['marketyear']
        attr_size_color_list = param['sizecolorlist']

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            getGoods = GetGoods()
            getPhoto = GetGoodsPhoto()
            getAttr = GetGoodsAttr()
            netGoodsDetail = getGoods.getGoodsById(goods_id=goods_id)
            if not netGoodsDetail:
                baseResponse.code = ResponseCode.fail_goods_not_found
                baseResponse.desc = ResponseCode.fail_goods_not_found_desc
            else:
                # 更新数据
                dbGoods = DbGoods()
                dbGoods.goods_id = netGoodsDetail.id
                if cate_id:
                    dbGoods.cate_id = cate_id
                if brand_id:
                    dbGoods.brand_id = brand_id
                if goods_name:
                    dbGoods.goods_name = goods_name
                if market_price:
                    dbGoods.market_price = market_price
                if current_price:
                    dbGoods.current_price = current_price
                if sale_count:
                    dbGoods.sale_count = sale_count
                if stock_num:
                    dbGoods.stock_num = stock_num
                if status:
                    dbGoods.status = status
                if goods_code:
                    dbGoods.goods_code = goods_code
                if goods_logo:
                    dbGoods.goods_logo = goods_logo
                if thum_logo:
                    dbGoods.thum_logo = thum_logo
                if keywords:
                    dbGoods.keywords = keywords
                #  photo
                dbPhotoThumList = []
                if photo_thum_list:
                    # delete first when update
                    getPhoto.deleteGoodsPhotoById(goods_id=dbGoods.goods_id)
                    for photo_thum in photo_thum_list:
                        dbGoodsPhoto = DbGoodsPhoto()
                        dbGoodsPhoto.photo = photo_thum['photos']
                        dbGoodsPhoto.thum_photo = photo_thum['thum_photo']
                        dbGoodsPhoto.goods_id = dbGoods.goods_id
                        dbPhotoThumList.append(dbGoodsPhoto)
                # attr
                dbGoodsAttrList = []
                if attr_size_color_list:
                    # delete first when update
                    getAttr.deleteGoodsAttr(dbGoods.goods_id)
                    for attr_size_color in attr_size_color_list:
                        dbGoodsAttr = DbAttribute()
                        attr_size = attr_size_color['goodssize']
                        attr_color = attr_size_color['goodscolor']
                        dbGoodsAttr.attr_size = attr_size
                        dbGoodsAttr.attr_color = attr_color
                        dbGoodsAttr.attr_market_year = attr_market_year
                        dbGoodsAttr.goods_id = dbGoods.goods_id
                        dbGoodsAttr.cate_id = dbGoods.cate_id
                        dbGoodsAttrList.append(dbGoodsAttr)
                updateResult = getGoods.updateToDb(goods=dbGoods)
                savePhotoResult = getPhoto.addGoodsPhotoList(dbPhotoThumList)
                saveAttrResult = getAttr.addGoodsAttrList(dbGoodsAttrList)
                if updateResult and savePhotoResult and saveAttrResult:
                    baseResponse.code = ResponseCode.op_success
                    baseResponse.desc = ResponseCode.op_success_desc
                else:
                    baseResponse.code = ResponseCode.fail_op_db_data
                    baseResponse.desc = ResponseCode.fail_op_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)


