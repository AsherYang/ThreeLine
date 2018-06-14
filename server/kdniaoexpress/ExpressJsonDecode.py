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
        dict = super(TrackDecode, self).decode(s)
        print dict
        baseResponse = ExpressResponse()
        trackResponse = ExpressTrackResponse()
        baseResponse.msg = dict['msg']
        baseResponse.code_http = dict['code_http']
        if 'EBusinessID' in dict['data']:
            trackResponse.EBusinessID = dict['data']['EBusinessID']
        if 'OrderCode' in dict['data']:
            trackResponse.OrderCode = dict['data']['OrderCode']
        if 'ShipperCode' in dict['data']:
            trackResponse.ShipperCode = dict['data']['ShipperCode']
        if 'LogisticCode' in dict['data']:
            trackResponse.LogisticCode = dict['data']['LogisticCode']
        if 'Success' in dict['data']:
            trackResponse.Success = dict['data']['Success']
        if 'Reason' in dict['data']:
            trackResponse.Reason = dict['data']['Reason']
        if 'State' in dict['data']:
            trackResponse.State = dict['data']['State']
        tracesList = []
        for tracesTmp in dict['data']['Traces']:
            traces = ExpressTraces()
            if 'AcceptTime' in tracesTmp.keys():
                traces.AcceptTime = tracesTmp['AcceptTime']
            if 'AcceptStation' in tracesTmp.keys():
                traces.AcceptStation = tracesTmp['AcceptStation']
            if 'Remark' in tracesTmp.keys():
                traces.Remark = tracesTmp['Remark']
            tracesList.append(traces)
        trackResponse.Traces = tracesList
        baseResponse.data = trackResponse
        return baseResponse

