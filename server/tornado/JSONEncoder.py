#!/usr/bin/python
# -*- coding:utf-8 -*-

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
            # print type(contentData)
            realContent = []
            if isinstance(contentData, list):
                for data in contentData:
                    if isinstance(data, ContentData):
                        string = {'id': data.id, 'syncKey': data.syncKey, 'updateTime': data.updateTime,
                                  'title': data.title, 'content': data.content, 'author': data.author,
                                  'imagePath': data.imagePath, 'songName': data.songName, 'singer': data.singer}
                        realContent.append(string)
            elif isinstance(contentData, basestring):
                realContent = contentData
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
