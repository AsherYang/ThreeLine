#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   FFStore Server
"""

import os
import subprocess
import threading
import MySQLdb
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb
from tornado.options import define, options

from constant import DbConstant
from util.SendMsgEmail import SendEmail
from db.DbUser import DbUser
from db.UserDao import UserDao
from FFStoreJsonEncoder import *
from BaseResponse import BaseResponse
from constant import ResponseCode
import WeiChatMsg
from ffstore.net.GetCategory import GetCategory
from ffstore.net.GetGoods import GetGoods

define("debug", default=False, help='Set debug mode', type=bool)
# 服务器使用Supervisor＋nginx 三行情书配置多端口：8888｜8889｜8890｜8891, 上好微店端口：10001|10002
# FFStore端口: 20001|20002|20003
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
class pushMsgHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        json_str = '{"status":"success"}'
        self.write(json_str)
    def post(self, *args, **kwargs):
        json_str = '{"status":"success"}'
        self.write(json_str)

"""
receive weiChat push msg
@see {#https://mp.weixin.qq.com/wxopen/devprofile?action=get_callback&token=1304670207&lang=zh_CN}
url: https://shmall.fansdroid.net/weichat/push/msg
Token: token20170907shmallweichatkey
EncodingAESKey: Cx4Nqorw8Gw7wWtIgPSoVbmLwJb20UnUkh36CKY0JPn
"""
class weiChatMsgHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        print "signature = " + signature + " , timestamp = " + timestamp + " , nonce = " + nonce + " , echostr = " + echostr
        weiChatMsg = WeiChatMsg(signature, timestamp, nonce)
        if weiChatMsg.checkSignature():
            print 'ok. check success'
            self.write(echostr)
            self.sendEmail('FFStore有转发消息，请查看')
        else:
            print 'false. check fail'
            self.write('false. check fail')

    def post(self, *args, **kwargs):
        json_str = 'do not call post msg at weiChat msg'
        self.write(json_str)
        self.sendEmail('FFStore有转发消息，请查看')

    def sendEmail(self, msg):
        sendEmail = SendEmail()
        # sendEmail(content=msg)
        thr = threading.Thread(target=sendEmail, args=[msg])    # open new thread
        thr.start()

"""
get category
"""
class getCategoryHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        getCategory = GetCategory()
        categoryList = getCategory.doGetCategory()
        baseResponse = BaseResponse()
        for category in categoryList:
            baseResponse.data.append(category)
        json_str = json.dumps(baseResponse, cls=CategoryEncoder)
        self.write(json_str)

"""
get all goods
"""
class getAllGoodsHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        getGoods = GetGoods()
        # todo getAllGoods
        allGoodsList = getGoods.getAllGoods()
        baseResponse = BaseResponse()
        baseResponse.code = "000001"
        baseResponse.desc = "successfully"
        for goods in allGoodsList:
            baseResponse.data.append(goods)
        json_str = json.dumps(baseResponse, cls=AllGoodsEncoder)
        self.write(json_str)

"""
get home page discover list
首页封面列表，拿到的数据是category表中 cate_show_type 字段
https://sujiefs.com//api/mall/discoverList?page=1&size=10&sign=1c0c67948371e91081fac39137d990c4&time=20180430145004
"""
class getHomeDiscoverListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = self.get_argument('page')
        size = self.get_argument('size')
        getCategory = GetCategory()
        homeDiscoverList = getCategory.getHomeDiscoverList(page_num=page, page_size=size)
        baseResponse = BaseResponse()
        baseResponse.code = ResponseCode.op_success
        baseResponse.desc = ResponseCode.op_success_desc
        homeDiscoverCount = getCategory.getHomeDiscoverCount()
        page_total = (homeDiscoverCount / size) + (1 if homeDiscoverCount % size > 0 else 0)
        baseResponse.page_total = page_total
        for homeDiscover in homeDiscoverList:
            baseResponse.append(homeDiscover)
        json_str = json.dumps(baseResponse, cls=HomeDiscoverEncoder)
        self.write(json_str)

"""
点击封面列表进入的分类展示专区
分类列表，拿到的数据是 goods 表中对应cate_code 字段的数据
sort: 排序字段，根据 "综合","销量","价格"排序
skuval: "尺码"
https://sujiefs.com//api/home/hostGoodsList?page=1&size=10&cateCode=021&sort=1&skuval=&sign=694e9f6dec1f1d11475a5ac688d8d644&time=20180430155433
"""
class getHostGoodsListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = self.get_argument('page')
        size = self.get_argument('size')
        cateCode = self.get_argument('cateCode')
        sort = self.get_argument('sort')
        skuval = self.get_argument('skuval')
        getGoods = GetGoods()
        netHostGoods = getGoods.getHostGoods(cateCode, skuval, page, size, sort)
        baseResponse = BaseResponse()
        baseResponse.code = ResponseCode.op_success
        baseResponse.desc = ResponseCode.op_success_desc
        hostGoodsCount = getGoods.getGoodsCountByCate(cateCode)
        page_total = (hostGoodsCount / size) + (1 if hostGoodsCount % size > 0 else 0)
        baseResponse.page_total = page_total
        baseResponse.data = netHostGoods
        json_str = json.dumps(baseResponse, cls=HostGoodsEncoder)
        self.write(json_str)

"""
save user to db
"""
class saveUserHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        userName = self.get_argument('name', '')
        phone = self.get_argument('phone', '')
        address = self.get_argument('address', '')
        user = DbUser()
        user.user_name = userName
        user.user_tel = phone
        user.address = address
        userDao = UserDao()
        result = userDao.operate(user)
        baseResponse = BaseResponse()
        if result:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
        elif not phone:
            baseResponse.code = ResponseCode.invalid_user_phone
            baseResponse.desc = ResponseCode.invalid_user_phone_desc
        elif not address:
            baseResponse.code = ResponseCode.invalid_user_address
            baseResponse.desc = ResponseCode.invalid_user_address_desc
        else:
            baseResponse.code = ResponseCode.update_user_info_error
            baseResponse.desc = ResponseCode.update_user_info_error_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)

class updateUserCostHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        phone = self.get_argument('user_tel', '')
        cost = self.get_argument('cost_this_time', '')
        user = DbUser()
        user.user_tel = phone
        userDao = UserDao()
        result = userDao.updateUserCost(user, cost)
        if result:
            print 'add user cost successfully!'
        else:
            print ResponseCode.add_user_cost_error_desc

class CustomApplication(tornado.web.Application):
    def __init__(self, debug=False):
        handlers = [
            (r"/", MainHandler),
            (r'/push/msg', pushMsgHandler),
            (r'/weichat/push/msg', weiChatMsgHandler),
            (r'/get/category', getCategoryHandler),
            (r'/mall/discoverList', getHomeDiscoverListHandler),
            (r'/home/hostGoodsList', getHostGoodsListHandler),
            # (r'/get/allgoods', getAllGoodsHandler),
            (r'/save/user', saveUserHandler),
            (r'/update/user/cost', updateUserCostHandler),
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
            self.db.get('select count(*) from ffstore_size')
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
