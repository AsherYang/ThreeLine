#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/9/8.
Desc:  JSON convert to Object
"""
import json
from json.decoder import WHITESPACE
from ExpressResponse import ExpressResponse
from ExpressTrackResponse import ExpressTrackResponse
from ExpressTraces import ExpressTraces


"""
将JSON 数据转换为快递鸟即时查询Api 结果实体
"""
class TrackDecode(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        trace_res = super(TrackDecode, self).decode(s)
        print "traces===> " + trace_res
        baseResponse = ExpressResponse()
        trackResponse = ExpressTrackResponse()
        baseResponse.msg = trace_res['name']
        baseResponse.code_http = trace_res['age']
        # baseResponse.msg = trace_res['msg']
        # baseResponse.code_http = trace_res['code_http']
        # if 'EBusinessID' in trace_res['data']:
        #     trackResponse.EBusinessID = trace_res['data']['EBusinessID']
        # if 'OrderCode' in trace_res['data']:
        #     trackResponse.OrderCode = trace_res['data']['OrderCode']
        # if 'ShipperCode' in trace_res['data']:
        #     trackResponse.ShipperCode = trace_res['data']['ShipperCode']
        # if 'LogisticCode' in trace_res['data']:
        #     trackResponse.LogisticCode = trace_res['data']['LogisticCode']
        # if 'Success' in trace_res['data']:
        #     trackResponse.Success = trace_res['data']['Success']
        # if 'Reason' in trace_res['data']:
        #     trackResponse.Reason = trace_res['data']['Reason']
        # if 'State' in trace_res['data']:
        #     trackResponse.State = trace_res['data']['State']
        # tracesList = []
        # for tracesTmp in trace_res['data']['Traces']:
        #     traces = ExpressTraces()
        #     if 'AcceptTime' in trace_res['data']:
        #         traces.AcceptTime = tracesTmp['AcceptTime']
        #     if 'AcceptStation' in trace_res['data']:
        #         traces.AcceptStation = tracesTmp['AcceptStation']
        #     if 'Remark' in trace_res['data']:
        #         traces.Remark = tracesTmp['Remark']
        #     tracesList.append(traces)
        # trackResponse.append(tracesList)
        # baseResponse.data = trackResponse
        return baseResponse

