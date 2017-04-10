#!/user/bin/env python
#-*- coding: utf-8 -*-

# Author: AsherYang
# Email:  1181830457@qq.com
# Date:   2017/4/10
# Desc:   hello world for tornado

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.autoreload
from tornado.options import define, options
import json

define("debug", default=True, help='debug mode', type=bool)
define("port", default=8888, help='run on the give port', type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello AsherYang , nice to meet you!")

class OtherHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=416, log_message="test other", reason="unKnow request, please wait for 127.0.0.1")

class LastDataHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = [{'a':"A", 'b':(2,4), 'c':3.0, 'd':"AsherYang"}]
        json_str = json.dumps(data)
        self.write(json_str)

class CustomApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r'/getlastdata', LastDataHandler),
            (r"/.*", OtherHandler),
        ]
        settings = {
            "cookie_secret": '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
            "xsrf_cookies": True,
            "debug": options.debug,
        }
        super(CustomApplication, self).__init__(handlers=handlers, settings=settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication())
    http_server.listen(options.port)
    # if settings.get("debug"):
    #     tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
