#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : delete category and the category goods tornado handler

manager api handler
"""
import sys
sys.path.append('../')
import tornado.web
from constant import ResponseCode
from FFStoreJsonEncoder import *

from mgrsys.PermissionManager import PermissionManager
from net.GetGoods import GetGoods
from net.GetAdverts import GetAdverts

"""
删除商品分类，及该分类下的所有商品
管理员操作，注意需要严格的权限验证。
"""
class ManagerDeleteCateAndGoodsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        sign = param['sign']
        time = param['time']
        admin_tel = param['tel']
        sms_pwd = param['sms']
        cate_id = param['cate_id']
        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            getGoods = GetGoods()
            # 删除分类及商品
            deleteResult = getGoods.deleteCateAndGoods(cate_id)
            # 删除广告banner, 无论是否删除(不管结果)
            getAdverts = GetAdverts()
            getAdverts.deleteAdvertsByCateId(cate_id)
            if deleteResult:
                baseResponse.code = ResponseCode.op_success
                baseResponse.desc = ResponseCode.op_success_desc
            else:
                baseResponse.code = ResponseCode.op_fail_db_data
                baseResponse.desc = ResponseCode.op_fail_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)
