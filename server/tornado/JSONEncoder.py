#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   json encoder for custom class
"""

from ContentData import ContentData
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ContentData):
            return {'code': obj.code, 'desc': obj.desc,
                     'data': [{'syncKey': obj.syncKey, 'updateTime': obj.updateTime, 'title': obj.title,
                               'content': obj.content, 'author': obj.author, 'imagePath': obj.imagePath}]}
        else:
            return json.JSONEncoder.default(self, obj)
