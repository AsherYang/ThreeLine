#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/4/10
Desc:   server on tornado
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
from BaseResponse import BaseResponse
from JSONEncoder import JSONEncoder

define("debug", default=False, help='Set debug mode', type=bool)
# 服务器使用Supervisor＋nginx 配置多端口：8888｜8889｜8890｜8891
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
        baseResponse = BaseResponse()
        baseResponse.code = "000001"
        baseResponse.desc = "successfully"
        # load from db
        self.application.syncKey = self.application.syncKey + 1
        insert = 'insert into contents (syncKey, updateTime, title, content, author, imagePath, songName, singer) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' %(self.application.syncKey, datetime.datetime.now(), 'test', 'this is a test msg', 'Asher', '/image', 'what fuck', 'AsherYang')
        self.application.db.execute(insert)
        cmd = 'select * from contents'
        contents = self.application.db.query(cmd)
        # print articles
        for content in contents:
            contentData = ContentData()
            contentData.id = content["id"]
            contentData.syncKey = content["syncKey"]
            contentData.updateTime = content["updateTime"]
            contentData.title = content["title"]
            contentData.content = content["content"]
            contentData.author = content["author"]
            contentData.imagePath = content["imagePath"]
            contentData.songName = content['songName']
            contentData.singer = content['singer']
            baseResponse.data.append(contentData)
        json_str = json.dumps(baseResponse, cls=JSONEncoder)
        # print json_str
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
        # 定义一个临时变量
        self.syncKey = 0

    """
      在application中调用，先进行查询，如果报异常说明表没有创建，则进行创建表结构。
      这种方式保证数据表只创建一次。
    """
    def create_tables(self):
        try:
            self.db.get('select count(*) from contents')
        except MySQLdb.ProgrammingError:
            subprocess.check_call([
                'mysql',
                '--host=' + options.mysql_host,
                '--database=' + options.mysql_database,
                '--user=' + options.mysql_user,
                '--password=' + options.mysql_password,
            ], stdin=open(os.path.join(os.path.dirname(__file__), 'schema.sql')))


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
