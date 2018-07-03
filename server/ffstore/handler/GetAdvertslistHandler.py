#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/29
Desc  : get adverts list tornado handler

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
from net.GetAdverts import GetAdverts


"""
首页获取广告列表
https://sujiefs.com//api/adverts/list?sign=d35e9a2a0a110e02e20b7407c11f6aa5&time=20180626011306
"""
class GetAdvertslistHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        logging = LogUtil().getLogging()
        baseResponse = BaseResponse()
        md5Util = MD5Util()
        if sign == md5Util.md5Signature(time):
            getAdverts = GetAdverts()
            netAdvertsList = getAdverts.getLastAdverts(6)
            logging.info("---> netAdvertsList: " + str(netAdvertsList))
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = netAdvertsList
        else:
            baseResponse.code = ResponseCode.fail_check_api_md5
            baseResponse.desc = ResponseCode.fail_check_api_md5_desc
        json_str = json.dumps(baseResponse, cls=AdvertsEncoder)
        self.write(json_str)
