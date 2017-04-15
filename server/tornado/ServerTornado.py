#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/10
Desc:   hello world for tornado
"""

import os
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.autoreload
from tornado.options import define, options
import json
import subprocess
import torndb
import MySQLdb
import datetime

from ContentData import ContentData
from JSONEncoder import JSONEncoder

define("debug", default=False, help='Set debug mode', type=bool)
define("port", default=8888, help='Run on the give port', type=int)
define("mysql_host", default='127.0.0.1', help='mysql host IP')
define("mysql_user", default='root', help='db user name')
define("mysql_password", default='ouyangfan', help='db user password')
define("mysql_database", default='threeline', help='db name')

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello AsherYang , nice to meet you!")

class OtherHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=416, log_message="test other", reason="unKnow request, please wait for 127.0.0.1")

"""
usefully
[{"a": "A", "c": 3.0, "b": [2, 4], "d": "AsherYang"}]
{"code": "000001", "data": [{"syncKey": 10010, "updateTime": 1492017462}], "desc": "successfully"}
"""
class LastDataHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # data = [{'a':"A", 'b':(2,4), 'c':3.0, 'd':"AsherYang"}]
        contentData = ContentData()
        contentData.code = "000001"
        contentData.desc = "successfully"
        # load from db
        insert = 'insert into articles (syncKey, updateTime, title, content, author, imagePath) values("%s", "%s", "%s", "%s", "%s", "%s")' %("1", datetime.datetime.now(), 'test', 'this is a test msg', 'Asher', '/image')
        self.application.db.execute(insert)
        cmd = 'select * from articles'
        articles = self.application.db.query(cmd)
        # print articles
        for article in articles:
            contentData.syncKey = article["syncKey"]
            contentData.updateTime = article["updateTime"]
            contentData.title = article["title"]
            contentData.content = article["content"]
            contentData.author = article["author"]
            contentData.imagePath = article["imagePath"]
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
        super(CustomApplication, self).__init__(handlers=handlers, **settings)
        self.db = torndb.Connection(host=options.mysql_host, database=options.mysql_database, user=options.mysql_user,
                                    password=options.mysql_password)
        self.create_tables()

    """
      在application中调用，先进行查询，如果报异常说明表没有创建，则进行创建表结构。
      这种方式保证数据表只创建一次。
    """
    def create_tables(self):
        try:
            self.db.get('select count(*) from articles')
        except MySQLdb.ProgrammingError:
            subprocess.check_call([
                'mysql',
                '--host=' + options.mysql_host,
                '--database=' + options.mysql_database,
                '--user=' + options.mysql_user,
                '--password=' + options.mysql_password,
            ], stdin=open(os.path.join(os.path.dirname(__file__), 'schema.sql')))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(debug=options.debug))
    http_server.listen(options.port)
    loop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start()
    loop.start()

if __name__ == '__main__':
    main()
