#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/6/4
Desc  : host goods 接口返回的参数信息
https://sujiefs.com//api/home/hostGoodsList?page=1&size=10&cateCode=021&sort=1&skuval=&sign=694e9f6dec1f1d11475a5ac688d8d644&time=20180430155433

/**
 * category : category 实体bean， 包含：
            code： 022 ----> categoryCode
            name:  春夏新品专区 ----> categoryName
            logo:  http://sujiefs.com/upload/images/20180322/201803221134300716543.jpg
            id  :  2c9257a16126d14701612b52808100d6 ----> categoryId
            attrs : [{"attrValList":[{"attrName":"品牌","attrNameId":213,"attrVal":"素洁","id":556}],"attrName":{"attrName":"品牌","categoryCode":"022","id":213}},{"attrValList":[{"attrName":"年份季节","attrNameId":214,"attrVal":"2018春季新款","id":557}],"attrName":{"attrName":"年份季节","categoryCode":"022","id":214}}]
 *  list    : goods 商品实体 bean 集合
            marketPrice  ： 119
            saleCount    ： 6
            businessName ： 广州素洁服饰公司
            businessId   ： 4028800457b6cf7a0157b7998c39001d
            thumLogo     ： http://sujiefs.com/upload/images/20180423/201804231129454571221_thumbnail.jpg
            title        ： 新款韩版印花字母短款T恤衫 T18C076
            evaluateCount： 0
            price        ： 63
            name         ： 新款韩版印花字母短款T恤衫  T18C076
            stockNum     ： 80
            wholePrice   ： 60
            logo         ： http://sujiefs.com/upload/images/20180423/201804231129454571221.jpg
            id           ： 2c9257a16136c3d60162f09204f04e9f
 */
"""


class NetHostGoods:

    def __init__(self):
        self._dbCategory = None
        self._dbGoodsList = None
        self._dbBrandList = None

    @property
    def dbCategory(self):
        return self._dbCategory

    @dbCategory.setter
    def dbCategory(self, value):
        self._dbCategory = value

    @property
    def dbGoodsList(self):
        return self._dbGoodsList

    @dbGoodsList.setter
    def dbGoodsList(self, value):
        self._dbGoodsList = value

    @property
    def dbBrandList(self):
        return self._dbBrandList

    @dbBrandList.setter
    def dbBrandList(self, value):
        self._dbBrandList = value

    # append to data,
    # @see http://stackoverflow.com/questions/16380575/python-decorating-property-setter-with-list
    def appendGoods(self, value):
        return self.dbGoodsList + [value]

    # extend 只能是一个列表
    def extendGoods(self, value):
        return self.dbGoodsList.extend(value)

    def appendBrand(self, value):
        return self.dbBrandList + [value]

    def extendBrand(self, value):
        return self.dbBrandList.extend(value)
