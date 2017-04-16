#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   json encoder for custom class
"""

import json

from BaseResponse import BaseResponse
from ContentData import ContentData


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseResponse):
            contentData = obj.data
            realContent = []
            for data in contentData:
                if isinstance(data, ContentData):
                    string = {'syncKey': data.syncKey, 'updateTime': data.updateTime, 'title': data.title,
                            'content': data.content, 'author': data.author, 'imagePath': data.imagePath}
                    realContent.append(string)
                else:
                    realContent.append('unknown data type')
            return {'code': obj.code, 'desc': obj.desc,
                    'data': realContent}
            # if isinstance(contentData, list):
            #     print contentData[0].author
            # else:
            #     print type(contentData)
        else:
            return json.JSONEncoder.default(self, obj)
