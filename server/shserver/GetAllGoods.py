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
import GetToken
import OpenRequest
import TokenConstant
from Category import Category
from ShJsonDecode import categoryDecode

"""
从微店获取所有商品
url = https://api.vdian.com/api?param={"showNoCate":"0"}&public={"method":"weidian.cate.get.list","access_token":"9882ff6e635aac4740646cf93f2389320007487713","version":"1.0"}
"""
def getAllGoodsFromNet():
    pageNum = 1
    orderby = 1
    page_size = 50



# 微店提供的方法
def vdianItemListGet(page_num, orderby, page_size, version="1.0", path="api"):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    param = {"page_num": page_num, "orderby": orderby, "page_size": page_size}
    pub = {"method": "vdian.item.list.get", "access_token": GetToken.doGetToken(), "version": version, "lang": "python",
           "sdkversion": TokenConstant.version}
    url = "%s%s?param=%s&public=%s" % (TokenConstant.domain, path, param, pub)
    body = OpenRequest.http_get(url, header=header)
    pageGoods = json.loads(body, "utf8")
    return pageGoods


"""
从数据库获取商品
"""
def getAllGoodsFromDb():
    print '--- getCategoryFromDb start ---'
    query = "select * from sh_category"
    results = DbUtil.query(query)
    print results
    if results is None:
        return None
    categoryList = []
    for row in results:
        category = Category()
        row_id = row[0]
        cate_id = row[1]
        cate_name = row[2]
        parent_id = row[3]
        parent_cate_name = row[4]
        sort_num = row[5]
        cate_item_num = row[6]
        description = row[7]
        listUrl = row[8]
        shopName = row[9]
        shopLogo = row[10]
        updateTime = row[11]
        category.cate_id = cate_id
        category.cate_name = cate_name
        category.parent_id = parent_id
        category.parent_cate_name = parent_cate_name
        category.sort_num = sort_num
        category.cate_item_num = cate_item_num
        category.description = description
        category.listUrl = listUrl
        category.shopName = shopName
        category.shopLogo = shopLogo
        category.update_time = updateTime
        categoryList.append(category)
        # print "row_id = %s, access_token = %s, expire_in = %s, update_time = %s " %(row_id, access_token, expire_in, update_time)
    return categoryList


"""
保存商品进数据库
"""
def saveAllGoodsToDb(categoryList=None):
    print '--- saveAllGoodsToDb start ---'
    if categoryList is None:
        print "categoryList is None could not save to db."
        return
    else:
        insert = 'insert into sh_category (cate_id, cate_name, parent_id, parent_cate_name, sort_num, cate_item_num,' \
                 ' description, listUrl, shopName, shopLogo, update_time) '
        sql_select_str = ''
        currentTime = int(time.time())
        for category in categoryList:
            sql_select_str += "SELECT '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' union " \
                              % (category.cate_id, category.cate_name, category.parent_id, category.parent_cate_name,
                                 category.sort_num, category.cate_item_num, category.description, category.listUrl,
                                 category.shopName, category.shopLogo, currentTime)
        # 拼接sql 语句
        insert = insert + sql_select_str
        # 截取字符串
        insert = insert[:-6]
        # 保存category 需要先清空数据
        delete = 'delete from sh_category;'
        DbUtil.delete(delete)
        DbUtil.insert(insert)


"""
商品 更新策略：
每天只更新一次
返回值：当前有效的 goods list
"""
def doGetCategory():
    currentTime = int(time.time())
    allGoodsList = getAllGoodsFromDb()
    # 更新间隔 1天 = 24 * 60 * 60
    updateInterval = 24 * 60 * 60
    print currentTime
    if allGoodsList is None:
        print "categoryList is None 正在更新"
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
    doGetCategory()
    # categoryNetList = getCategoryFromNet()
    # saveCategoryToDb(categoryNetList)
