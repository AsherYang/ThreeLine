#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/30
Desc:   商品排序

sort: 排序字段，根据 "综合","销量","价格"排序
"""

# 综合排序，处理为按照上新时间排列，最新的展示在最前面(_id 越大说明上新时间越近，_id 降序)
SORT_COMMON = 0
# 价格降序排序
SORT_PRICE_DOWN = 1
# 价格升序排序
SORT_PRICE_UP = 2
# 按销量排序，从高到低
SORT_SALE_COUNT = 3


