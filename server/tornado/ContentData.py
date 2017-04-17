#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/11
Desc:   Content to response to client
"""


class ContentData():
    @property
    def id(self):
        return self.id

    @property
    def id(self, value):
        self.id = value

    @property
    def syncKey(self):
        return self.syncKey

    @property
    def syncKey(self, value):
        self.syncKey = value

    @property
    def updateTime(self):
        return self.updateTime

    @property
    def updateTime(self, value):
        self.updateTime = value

    @property
    def title(self):
        return self.title

    @property
    def title(self, value):
        self.title = value

    @property
    def content(self):
        return self.content

    @property
    def content(self, value):
        self.content = value

    @property
    def author(self):
        return self.author

    @property
    def author(self, value):
        self.author = value

    @property
    def imagePath(self):
        return self.imagePath

    @property
    def imagePath(self, value):
        self.imagePath = value

    @property
    def songName(self):
        return self.songName

    @property
    def songName(self, value):
        self.songName = value

    @property
    def singer(self):
        return self.singer

    @property
    def singer(self, value):
        self.singer = value
