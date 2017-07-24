#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   shanghao server on tornado
"""

import os
import subprocess

import MySQLdb
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb
from tornado.options import define, options

define("debug", default=False, help='Set debug mode', type=bool)
# 服务器使用Supervisor＋nginx 配置多端口：8888｜8889｜8890｜8891, 上好微店端口：10001|10002
define("port", default=10001, help='Run on the give port', type=int)
define("mysql_host", default='127.0.0.1', help='mysql host IP')
define("mysql_user", default='root', help='db user name')
define("mysql_password", default='ouyangfan', help='db user password')
# 设置新数据库时，需要在服务器创建对应的数据库
define("mysql_database", default='shanghao', help='db name')


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello AsherYang , nice to meet you!")


class OtherHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=416, log_message="test other",
                                    reason="unKnow request, please wait for http://www.fansdroid.net")


"""
 test push data
"""
class pushMsgHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        json_str = '{"status":"success"}'
        self.write(json_str)


class CustomApplication(tornado.web.Application):
    def __init__(self, debug=False):
        handlers = [
            (r"/", MainHandler),
            (r'/push/msg', pushMsgHandler),
            (r"/.*", OtherHandler),
        ]
        settings = {
            # "cookie_secret": '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
            # "xsrf_cookies": True,
            "debug": debug,
        }
        super(CustomApplication, self).__init__(handlers=handlers, **settings)
        self.db = torndb.Connection(host=options.mysql_host, database=options.mysql_database, user=options.mysql_user,
                                    password=options.mysql_password)
        self.create_tables()
        # 定义一个临时变量,syncKey is wrong, because of multiprocess application
        self.syncKey = 0

    """
      在application中调用，先进行查询，如果报异常说明表没有创建，则进行创建表结构。
      这种方式保证数据表只创建一次。
    """

    def create_tables(self):
        try:
            self.db.get('select count(*) from sh_user')
        except MySQLdb.ProgrammingError:
            subprocess.check_call([
                'mysql',
                '--host=' + options.mysql_host,
                '--database=' + options.mysql_database,
                '--user=' + options.mysql_user,
                '--password=' + options.mysql_password,
            ], stdin=open(os.path.join(os.path.dirname(__file__), 'schema_sh.sql')))


def main():
    # 解析命令行参数，比如设置了port会使用命令行port配置覆盖，若没有设置，则使用define中默认值
    # python ServerTornado.py --port=8889，会启用实例监听8889端口，浏览器等访问8889端口会被监听
    # 所以服务器配置了4端口运行命令，都可以监听运行
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(debug=options.debug))
    http_server.listen(options.port)
    loop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start()
    loop.start()


if __name__ == '__main__':
    main()
