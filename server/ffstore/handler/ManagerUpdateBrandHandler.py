#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/5
Desc:   后台管理系统，更新商品分类handler

manager api handler
"""

import sys
sys.path.append('../')
import tornado.web
from constant import ResponseCode
from FFStoreJsonEncoder import *

from net.GetBrand import GetBrand
from mgrsys.PermissionManager import PermissionManager


class ManagerUpdateBrandHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        sign = param['sign']
        time = param['time']
        admin_tel = param['tel']
        sms_pwd = param['sms']

        brand_id = param['brand_id']
        brand_name = param['brand_name']
        brand_logo = param['brand_logo']

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            getbrand = GetBrand()
            dbBrand = getbrand.queryBrandById(brand_id=brand_id)
            if not dbBrand:
                baseResponse.code = ResponseCode.fail_cate_not_found
                baseResponse.desc = ResponseCode.fail_cate_not_found_desc
            else:
                # 更新数据
                if brand_name:
                    dbBrand.brand_name = brand_name
                if brand_logo:
                    dbBrand.brand_logo = brand_logo
                updateResult = getbrand.updateBrand(dbBrand=dbBrand)
                if updateResult:
                    baseResponse.code = ResponseCode.op_success
                    baseResponse.desc = ResponseCode.op_success_desc
                else:
                    baseResponse.code = ResponseCode.fail_op_db_data
                    baseResponse.desc = ResponseCode.fail_op_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)

