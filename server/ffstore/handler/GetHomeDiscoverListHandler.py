#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : get home discover list tornado handler

api handler
"""
import sys
sys.path.append('../')
import tornado.web
from BaseResponse import BaseResponse
from constant import ResponseCode
from FFStoreJsonEncoder import *

from util.LogUtil import LogUtil
from util.MD5Util import MD5Util
from net.GetCategory import GetCategory


"""
get home page discover list
首页封面列表，拿到的数据是category表中 cate_show_type 字段
https://sujiefs.com//api/mall/discoverList?page=1&size=10&sign=1c0c67948371e91081fac39137d990c4&time=20180430145004
"""
class GetHomeDiscoverListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        logging = LogUtil().getLogging()
        baseResponse = BaseResponse()
        md5Util = MD5Util()
        if sign == md5Util.md5Signature(time):
            getCategory = GetCategory()
            homeDiscoverList = getCategory.getHomeDiscoverList(page_num=page, page_size=size)
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            homeDiscoverCount = getCategory.getHomeDiscoverCount().get('count')
            logging.info('---> homeDiscoverCount: ' + str(homeDiscoverCount))
            page_total = (homeDiscoverCount / size) + (1 if homeDiscoverCount % size > 0 else 0)
            baseResponse.pageNum = page
            baseResponse.pageSize = size
            baseResponse.page_total = page_total
            baseResponse.totalCount = homeDiscoverCount
            if homeDiscoverList:
                for homeDiscover in homeDiscoverList:
                    baseResponse.append(homeDiscover)
        else:
            baseResponse.code = ResponseCode.fail_user_login
            baseResponse.desc = ResponseCode.fail_user_login_desc
        json_str = json.dumps(baseResponse, cls=HomeDiscoverEncoder)
        self.write(json_str)
