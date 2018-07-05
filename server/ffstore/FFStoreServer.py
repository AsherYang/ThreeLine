#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   FFStore Server
"""
import sys
sys.path.append('../')

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

from constant import DbConstant
from handler.WeiChatMsgHandler import WeiChatMsgHandler
from handler.GetUIDHandler import GetUIDHandler
from handler.GetWeiChatSessionHandler import GetWeiChatSessionHandler
from handler.UpdateUserCostHandler import UpdateUserCostHandler
from handler.SaveUserHandler import SaveUserHandler
from handler.GetAllGoodsHandler import GetAllGoodsHandler
from handler.SearchGoodsListHandler import SearchGoodsListHandler
from handler.GetGoodsDetailHandler import GetGoodsDetailHandler
from handler.GetHostGoodsListHandler import GetHostGoodsListHandler
from handler.GetHomeDiscoverListHandler import GetHomeDiscoverListHandler
from handler.GetAdvertslistHandler import GetAdvertslistHandler
from handler.GetCategoryHandler import GetCategoryHandler
from handler.WxLoginHandler import WxLoginHandler
from handler.WxSendMsgHandler import WxSendMsgHandler
from handler.ManagerAdminLoginHandler import ManagerAdminLoginHandler
from handler.ManagerAddAdvertsHandler import ManagerAddAdvertsHandler
from handler.ManagerDeleteAdvertsHandler import ManagerDeleteAdvertsHandler
from handler.ManagerAddCateHandler import ManagerAddCateHandler
from handler.ManagerDeleteCateAndGoodsHandler import ManagerDeleteCateAndGoodsHandler
from handler.ManagerUpdateCateHandler import ManagerUpdateCateHandler
from handler.ManagerAddGoodsHandler import ManagerAddGoodsHandler
from handler.ManagerDeleteGoodsHandler import ManagerDeleteGoodsHandler
from handler.ManagerUpdateGoodsHandler import ManagerUpdateGoodsHandler


define("debug", default=False, help='Set debug mode', type=bool)
# 服务器使用Supervisor＋nginx
# 三行情书配置多端口：8888｜8889｜8890｜8891
# 上好微店端口：10001|10002
# FFStore端口: 20001|20002|20003
# 微信报警端口: 9091
# pypi-server端口:9099
define("port", default=20001, help='Run on the give port', type=int)
define("mysql_host", default=DbConstant.dbHost, help='mysql host IP')
define("mysql_user", default=DbConstant.dbUser, help='db user name')
define("mysql_password", default=DbConstant.dbPwd, help='db user password')
# 设置新数据库时，需要在服务器创建对应的数据库
define("mysql_database", default=DbConstant.dbName, help='db name')


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello AsherYang is FFStore, nice to meet you!")


class OtherHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(status_code=416, log_message="test other",
                                    reason="unKnow request, please wait for http://www.oyf.name")


"""
 test push data
"""
class PushMsgHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        json_str = '{"status":"success"}'
        self.write(json_str)

    def post(self, *args, **kwargs):
        json_str = '{"status":"success"}'
        self.write(json_str)


class CustomApplication(tornado.web.Application):
    def __init__(self, debug=False):

        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "html"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "cookie_secret": '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
            "xsrf_cookies": True,
            "debug": debug,
        }

        # 接口不以 restful 形式，是因为我想把他分开到不同的类里面处理，便于前后台分开调用。逻辑更清晰。
        handlers = [
            (r"/", MainHandler),
            (r'/push/msg', PushMsgHandler),
            (r'/weichat/push/msg', WeiChatMsgHandler),
            (r'/get/category', GetCategoryHandler),
            (r'/api/adverts/list', GetAdvertslistHandler),
            (r'/api/mall/discoverList', GetHomeDiscoverListHandler),
            (r'/api/home/hostGoodsList', GetHostGoodsListHandler),
            (r'/api/mall/goods', GetGoodsDetailHandler),
            (r'/api/mall/searchGoodsList', SearchGoodsListHandler),
            # (r'/get/allgoods', GetAllGoodsHandler),
            (r'/save/user', SaveUserHandler),
            (r'/update/user/cost', UpdateUserCostHandler),
            (r'/api/weichat/jscode2session', GetWeiChatSessionHandler),
            (r'/get/uid', GetUIDHandler),
            (r'/wx/login', WxLoginHandler),
            (r'/wx/send/msg', WxSendMsgHandler),
            # 后台接口
            (r'/manager/admin/login', ManagerAdminLoginHandler),
            (r'/manager/adverts/add', ManagerAddAdvertsHandler),
            (r'/manager/adverts/delete', ManagerDeleteAdvertsHandler),
            (r'/manager/cate/add', ManagerAddCateHandler),
            (r'/manager/cate/delete/goods', ManagerDeleteCateAndGoodsHandler),
            (r'/manager/cate/update', ManagerUpdateCateHandler),
            (r'/manager/goods/add', ManagerAddGoodsHandler),
            (r'/manager/goods/delete', ManagerDeleteGoodsHandler),
            (r'/manager/goods/update', ManagerUpdateGoodsHandler),
            (r"/.*", OtherHandler),
        ]

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
            self.db.get('select count(*) from ffstore_attr')
        except MySQLdb.ProgrammingError:
            subprocess.check_call([
                'mysql',
                '--host=' + options.mysql_host,
                '--database=' + options.mysql_database,
                '--user=' + options.mysql_user,
                '--password=' + options.mysql_password,
            ], stdin=open(os.path.join(os.path.dirname(__file__), 'schema_ffstore.sql')))


def main():
    # 解析命令行参数，比如设置了port会使用命令行port配置覆盖，若没有设置，则使用define中默认值
    # python ServerTornado.py --port=8889，会启用实例监听8889端口，浏览器等访问8889端口会被监听
    # 所以服务器配置了4端口运行命令，都可以监听运行
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(debug=options.debug), xheaders=True)
    http_server.listen(options.port)
    loop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start()
    loop.start()


if __name__ == '__main__':
    main()
