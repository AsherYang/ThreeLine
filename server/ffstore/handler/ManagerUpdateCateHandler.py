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

from mgrsys.PermissionManager import PermissionManager
from net.GetCategory import GetCategory


class ManagerUpdateCateHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        sign = param['sign']
        time = param['time']
        admin_tel = param['tel']
        sms_pwd = param['sms']

        cate_code = param['catecode']
        parent_code = param['parentcode']
        cate_name = param['catename']
        cate_show_type = param['showtype']
        cate_logo = param['catelogo']

        permissionMgr = PermissionManager()
        baseResponse = permissionMgr.checkAdminPermissionWithLoginStatus(sign=sign, time=time,
                                                                         admin_tel=admin_tel, sms_pwd=sms_pwd)
        if baseResponse.code == ResponseCode.success_check_admin_permission:
            getCate = GetCategory()
            dbCate = getCate.getCategoryFromDb(cate_code=cate_code)
            if not dbCate:
                baseResponse.code = ResponseCode.fail_cate_not_found
                baseResponse.desc = ResponseCode.fail_cate_not_found_desc
            else:
                # 更新数据
                if parent_code:
                    dbCate.parent_code = parent_code
                if cate_name:
                    dbCate.cate_name = cate_name
                dbCate.cate_show_type = cate_show_type
                if cate_logo:
                    dbCate.cate_logo = cate_logo
                updateResult = getCate.updateCategoryToDb(category=dbCate)
                if updateResult:
                    baseResponse.code = ResponseCode.op_success
                    baseResponse.desc = ResponseCode.op_success_desc
                else:
                    baseResponse.code = ResponseCode.fail_op_db_data
                    baseResponse.desc = ResponseCode.fail_op_db_data_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)

