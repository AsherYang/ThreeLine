#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/8
Desc:   网络返回的基础码，对应解释
返回码以6位数字标识

000001 --> 表示成功

100000 - 199999 --> 预留字段

2xx --> 错误码
"""

# 操作成功
op_success = '000001'
op_success_desc = u'successfully'

# 无效用户电话号码
invalid_user_phone = '200001'
invalid_user_phone_desc = u'用户电话号码无效'

# 无效用户地址
invalid_user_address = '200002'
invalid_user_address_desc = u'用户地址无效'

# 更新用户信息出错
update_user_info_error = '200010'
update_user_info_error_desc = u'更新信息失败'

# 记录用户消费失败
add_user_cost_error = '200020'
add_user_cost_error_desc = u'记录用户消费失败'