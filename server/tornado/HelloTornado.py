#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/10
Desc:   hello world for tornado
"""

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.autoreload
from tornado.options import define, options
import json

from ContentData import ContentData
from JSONEncoder import JSONEncoder

define("debug", default=False, help='Set debug mode', type=bool)
define("port", default=8888, help='Run on the give port', type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello AsherYang , nice to meet you!")

class OtherHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=416, log_message="test other", reason="unKnow request, please wait for 127.0.0.1")

"""
[{"a": "A", "c": 3.0, "b": [2, 4], "d": "AsherYang"}]
[{"syncKey": 10010, "code": "200", "data": "AsherYang", "createTime": "2017/04/11", "desc": "successfully"}]
"""
class LastDataHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # data = [{'a':"A", 'b':(2,4), 'c':3.0, 'd':"AsherYang"}]
        contentData = ContentData()
        contentData.syncKey = 10010
        contentData.createTime = '2017/04/11'
        contentData.desc = "successfully"
        contentData.data = "AsherYang"
        json_str = json.dumps(contentData, cls=JSONEncoder)
        self.write(json_str)

class CustomApplication(tornado.web.Application):
    def __init__(self, debug=False):
        handlers = [
            (r"/", MainHandler),
            (r'/getlastdata', LastDataHandler),
            (r"/.*", OtherHandler),
        ]
        settings = {
            "cookie_secret": '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
            "xsrf_cookies": True,
            "debug": debug,
        }
        super(CustomApplication, self).__init__(handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(debug=options.debug))
    http_server.listen(options.port)
    loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start()
    loop.start()

if __name__ == '__main__':
    main()
