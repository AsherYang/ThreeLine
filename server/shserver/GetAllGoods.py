#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/7/24
Desc:   get weidian token
@see https://wiki.open.weidian.com/api#37

url = https://api.vdian.com/api?param={"page_num":1,"page_size":10,"orderby":1,"update_start":"2012-11-12 16:36:08","update_end":"2015-11-12 16:36:08","status":1}&public={"method":"vdian.item.list.get","access_token":"40be967eabb8057fc7975ed64895b5d900023716b1","version":"1.0","format":"json"}
必须为get 请求
"""
import json
import time

import DbUtil
from Goods import Goods
import OpenRequest
import TokenConstant
from ShJsonDecode import goodsDecode

"""
从微店获取所有商品
url = https://api.vdian.com/api?param={"showNoCate":"0"}&public={"method":"weidian.cate.get.list","access_token":"9882ff6e635aac4740646cf93f2389320007487713","version":"1.0"}
"""
allGoodsList = []
def getAllGoodsFromNet(pageNum=0, page_size=50, allGoodsSize=0, getedGoodsSize=0):
    orderby = 1
    print "-- allGoodsSize:%d , getedGoodsSize:%d --" %(allGoodsSize, getedGoodsSize)
    if allGoodsSize == 0 or allGoodsSize > getedGoodsSize:
        pageNum += 1
        htmlBody = vdianItemListGet(pageNum, orderby, page_size)
        # 返回每一页商品的Json数据
        pageGoodsJson = json.loads(htmlBody, "utf8")
        getedGoodsSize += pageGoodsJson['result']['item_num']
        allGoodsSize = pageGoodsJson['result']['total_num']
        # print pageGoodsJson
        goodsList = json.loads(htmlBody, cls=goodsDecode)
        # print "get goods perSize: %d , getedSize:%d,  totalSize: %d, cate_id: %s, cate_name:%s" \
        #       %(len(goodsList), int(getedGoodsSize), int(allGoodsSize), goodsList[0].cate_id, goodsList[0].cate_name)
        if goodsList:
            for goods in goodsList:
                allGoodsList.append(goods)
        # lastGoods = allGoodsList[len(allGoodsList)-1]
        # print "allGoodsList size %s , lastGoodsCateId: %s, lastGoodsCateName:%s " \
        #       %(len(allGoodsList), lastGoods.cate_id, lastGoods.cate_name)
        getAllGoodsFromNet(pageNum, allGoodsSize=allGoodsSize, getedGoodsSize=getedGoodsSize)

    return allGoodsList


# 微店提供的方法
def vdianItemListGet(page_num, orderby, page_size, version="1.0", path="api"):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    # GetToken.doGetToken()
    param = {"page_num": page_num, "orderby": orderby, "page_size": page_size}
    pub = {"method": "vdian.item.list.get", "access_token": "c79ec580a7e4e30eef74ed8b9ad93e7a0007487713",
           "version": version, "lang": "python",
           "sdkversion": TokenConstant.version}
    url = "%s%s?param=%s&public=%s" % (TokenConstant.domain, path, param, pub)
    body = OpenRequest.http_get(url, header=header)
    # pageGoods = json.loads(body, "utf8")
    return body


"""
从数据库获取商品
"""
def getAllGoodsFromDb():
    print '--- getAllGoodsFromDb start ---'
    query = "select * from sh_goods"
    results = DbUtil.query(query)
    print results
    if results is None:
        return None
    allGoodsList = []
    for row in results:
        goods = Goods()
        row_id = row[0]
        cate_id = row[1]
        cate_name = row[2]
        itemid = row[3]
        item_desc = row[4]
        item_name = row[5]
        imgs = row[6]
        price = row[7]
        update_time = row[8]

        goods.cate_id = cate_id
        goods.cate_name = cate_name
        goods.itemid = itemid
        goods.item_desc = item_desc
        goods.item_name = item_name
        goods.imgs = imgs
        goods.price = price
        goods.update_time = update_time

        allGoodsList.append(goods)
        # print "row_id = %s, access_token = %s, expire_in = %s, update_time = %s " %(row_id, access_token, expire_in, update_time)
    return allGoodsList


"""
保存商品进数据库
"""
def saveAllGoodsToDb(goodsList=None):
    print '--- saveAllGoodsToDb start ---'
    if goodsList is None or len(goodsList) == 0:
        print "categoryList is None could not save to db."
        return
    else:
        insert = 'insert into sh_goods (cate_id, cate_name, itemid, item_desc, item_name, imgs, price, update_time) '
        sql_select_str = ''
        currentTime = int(time.time())
        for goods in goodsList:
            sql_select_str += "SELECT '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' union " \
                              % (goods.cate_id, goods.cate_name, goods.itemid, goods.item_desc, goods.item_name,
                                 goods.imgs, goods.price, currentTime)
        # 拼接sql 语句
        insert = insert + sql_select_str
        # 截取字符串
        insert = insert[:-6]
        # 保存goods 需要先清空数据
        delete = 'delete from sh_goods;'
        DbUtil.delete(delete)
        DbUtil.insert(insert)


"""
商品 更新策略：
每天只更新一次
返回值：当前有效的 goods list
"""
def doGetAllGoods():
    currentTime = int(time.time())
    allGoodsList = getAllGoodsFromDb()
    # 更新间隔 1天 = 24 * 60 * 60
    updateInterval = 24 * 60 * 60
    print currentTime
    if allGoodsList is None:
        print "allGoodsList is None 正在更新"
        goodsNetList = getAllGoodsFromNet()
        saveAllGoodsToDb(goodsNetList)
        return goodsNetList

    lastTime = (int)(allGoodsList[0].update_time)
    if (currentTime - lastTime < updateInterval):
        print "从数据库中拿到 %d 条 all goods 数据" % (len(allGoodsList))
        return allGoodsList
    else:
        print "all goods list is 日期太久了 正在更新"
        goodsNetList = getAllGoodsFromNet()
        saveAllGoodsToDb(goodsNetList)
        return goodsNetList


if __name__ == '__main__':
    # doGetAllGoods()
    # allGoodsNetList = getAllGoodsFromNet()
    # saveAllGoodsToDb(allGoodsNetList)
    # delete = 'delete from sh_goods;'
    # DbUtil.delete(delete)
    query = "select * from sh_goods"
    results = DbUtil.query(query)
    print len(results)
    delete = 'delete from sh_goods'
    DbUtil.delete(delete)
    query = "select * from sh_goods"
    results = DbUtil.query(query)
    print len(results)