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
import threading

import MySQLdb
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb
from tornado.options import define, options

from WeiChatMsg import WeiChatMsg
from FFStoreJsonEncoder import *
from constant import DbConstant
from constant import ResponseCode
from constant import WxToken
from db.DbUser import DbUser
from net.GetUser import GetUser
from net.GetCategory import GetCategory
from net.GetGoods import GetGoods
from util.SendMsgEmail import SendEmail
from util import HttpUtil
from util.MD5Util import MD5Util
from util.LogUtil import LogUtil
from util.GenerateIDUtil import GenerateIDUtil

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

https://ffstore.oyfstore.com/weichat/push/msg
Token:token20180625ffstoreweichatkey
EncodingAESKey:oJ48WmISVWaf2Xt91GnkchfRwct2FdLcE7sS7VoXJga
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
        thr = threading.Thread(target=sendEmail, args=[msg])  # open new thread
        thr.start()

"""
获取微信服务器, 登录态 Session
https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code
ffstore 测试appid:wx72877ae8bdff79b0
ffstore 测试appSecret:35c17c2b6f81e7b03735f17f546820bc
参考微信 API 接口, wx.login()

例如:
https://api.weixin.qq.com/sns/jscode2session?appid=wx72877ae8bdff79b0&secret=35c17c2b6f81e7b03735f17f546820bc&js_code=023fYoP02NmKh011uaP02S4rP02fYoP6&grant_type=authorization_code
{"session_key":"yOgupOCOGJ367zpnw14ScQ==","openid":"oUQQ-5bFHPGeXNNgO1mQvEgRLaSY"}
"""
class getWeiChatSessionHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        jsCode = self.get_argument('jsCode')
        nickName = self.get_argument('nickName')
        sign = self.get_argument('sign')
        time = self.get_argument('time')
        md5Util = MD5Util(time)
        if sign == md5Util.md5Signature():
            logging = LogUtil().getLogging()
            logging.info('----> nickName: ' + nickName)
            httpUrl = 'https://api.weixin.qq.com/sns/jscode2session?='
            param = {"appid": WxToken.APP_ID, "secret": WxToken.APP_SECRET,
                     "js_code": str(jsCode), "grant_type": 'authorization_code'}
            body = HttpUtil.http_get(httpUrl, params=param)
            jsonBody = json.loads(body, "utf8")
            logging.info('----> jsonBody: ' + jsonBody)
        else:
            jsonBody = json.loads(u'校验失败', "utf8")
        self.write(jsonBody)


"""
get category
获取所有的分类，包括一级分类和二级分类
"""
class getCategoryHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        getCategory = GetCategory()
        categoryList = getCategory.doGetCategory()
        baseResponse = BaseResponse()
        if categoryList:
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
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        getCategory = GetCategory()
        homeDiscoverList = getCategory.getHomeDiscoverList(page_num=page, page_size=size)
        baseResponse = BaseResponse()
        baseResponse.code = ResponseCode.op_success
        baseResponse.desc = ResponseCode.op_success_desc
        homeDiscoverCount = getCategory.getHomeDiscoverCount().get('count')
        logging = LogUtil().getLogging()
        logging.info(homeDiscoverCount)
        page_total = (homeDiscoverCount / size) + (1 if homeDiscoverCount % size > 0 else 0)
        baseResponse.pageNum = page
        baseResponse.pageSize = size
        baseResponse.page_total = page_total
        baseResponse.totalCount = homeDiscoverCount
        if homeDiscoverList:
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
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        cateCode = self.get_argument('cateCode')
        sort = int(self.get_argument('sort'))
        skuval = self.get_argument('skuval')
        getGoods = GetGoods()
        netHostGoods = getGoods.getHostGoods(cateCode, skuval, page, size, sort)
        baseResponse = BaseResponse()
        if netHostGoods:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            hostGoodsCount = getGoods.getGoodsCountByCate(cateCode, skuval)
            page_total = (hostGoodsCount / size) + (1 if hostGoodsCount % size > 0 else 0)
            baseResponse.pageNum = page
            baseResponse.pageSize = size
            baseResponse.page_total = page_total
            baseResponse.totalCount = hostGoodsCount
            baseResponse.data = netHostGoods
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=HostGoodsEncoder)
        self.write(json_str)


"""
获取商品详情信息
https://sujiefs.com//api/mall/goods?id=2c9257a16136c3d6016348cc332b5e5d&sign=d1260c4c7c83415023bccdcc6b69f293&time=20180606221032
"""
class getGoodsDetailHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        goods_id = self.get_argument('id')
        getGoods = GetGoods()
        netGoodsDetail = getGoods.getGoodsById(goods_id)
        baseResponse = BaseResponse()
        if netGoodsDetail:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = netGoodsDetail
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=GoodsDetailEncoder)
        self.write(json_str)


"""
搜索商品
接口与返回值和 {@see getHostGoodsListHandler} 类似

https://sujiefs.com//api/mall/searchGoodsList?page=1&size=10&searchKeyWords=&cateCode=008005&sort=-1&skuval=&sign=d2ebecbb0a1c36b51b0b5a20a6a85588&time=20180610132307
"""
class searchGoodsListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = int(self.get_argument('page'))
        size = int(self.get_argument('size'))
        searchKeywords = self.get_argument('searchKeyWords')
        cateCode = self.get_argument('cateCode')
        sort = self.get_argument('sort')
        skuval = self.get_argument('skuval')
        getGoods = GetGoods()
        netSearchGoods = getGoods.getSearchGoodsList(searchKeywords, cateCode, skuval, page, size, sort)
        baseResponse = BaseResponse()
        if netSearchGoods:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            searchGoodsCount = getGoods.getGoodsCountByKeywords(searchKeywords, cateCode, skuval)
            page_total = (searchGoodsCount / size) + (1 if searchGoodsCount % size > 0 else 0)
            baseResponse.pageNum = page
            baseResponse.pageSize = size
            baseResponse.page_total = page_total
            baseResponse.totalCount = searchGoodsCount
            baseResponse.data = netSearchGoods
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=HostGoodsEncoder)
        self.write(json_str)
        pass


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
        result = GetUser().operateUser2Db(user)
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

"""
更新用户消费数据
"""
class updateUserCostHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        phone = self.get_argument('phone', '')
        cost = self.get_argument('cost_this_time', '')
        result = GetUser().updateUserCost(phone, cost)
        if result:
            print 'add user cost successfully!'
        else:
            print ResponseCode.add_user_cost_error_desc


# 删除商品分类，及该分类下的所有商品
class deleteCateAndGoodsHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        cate_id = self.get_argument('cate_id', '')
        getGoods = GetGoods()
        deleteResult = getGoods.deleteCateAndGoods(cate_id)
        baseResponse = BaseResponse()
        if deleteResult:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)


# 生成唯一的ID
class getUIDHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        generateIdUtil = GenerateIDUtil()
        uid = generateIdUtil.getUID()
        baseResponse = BaseResponse()
        if uid:
            baseResponse.code = ResponseCode.op_success
            baseResponse.desc = ResponseCode.op_success_desc
            baseResponse.data = str(uid)
        else:
            baseResponse.code = ResponseCode.op_fail
            baseResponse.desc = ResponseCode.op_fail_desc
        json_str = json.dumps(baseResponse, cls=StrEncoder)
        self.write(json_str)


class CustomApplication(tornado.web.Application):
    def __init__(self, debug=False):
        handlers = [
            (r"/", MainHandler),
            (r'/push/msg', pushMsgHandler),
            (r'/weichat/push/msg', weiChatMsgHandler),
            (r'/get/category', getCategoryHandler),
            (r'/mall/discoverList', getHomeDiscoverListHandler),
            (r'/home/hostGoodsList', getHostGoodsListHandler),
            (r'/mall/goods', getGoodsDetailHandler),
            (r'/mall/searchGoodsList', searchGoodsListHandler),
            # (r'/get/allgoods', getAllGoodsHandler),
            (r'/save/user', saveUserHandler),
            (r'/update/user/cost', updateUserCostHandler),
            (r'/delete/cate/goods', deleteCateAndGoodsHandler),
            (r'/api/wechat/jscode2session', getWeiChatSessionHandler),
            (r'/get/id', getUIDHandler),
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
