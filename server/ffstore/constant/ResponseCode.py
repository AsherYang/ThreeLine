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

一般错误以 "fail_xxx_xxx" 形式
非法权限操作以 "illegal_xxx_xxx" 形式
"""

# 操作成功
op_success = '000001'
op_success_desc = u'successfully'

# 操作失败
op_fail = '000002'
op_fail_desc = u'操作失败'

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

# 获取微信session_key 无效
fail_wx_session_key = '200100'
fail_wx_session_key_desc = u'微信鉴权失败'

fail_user_login = '200101'
fail_user_login_desc = u'用户名或者密码错误'

fail_user_out_of_date = '200102'
fail_user_out_of_date_desc = u'登陆已过期'

# 运维微信登陆失败, 请刷新后重试。关于运维微信与其他状态码并不在同一逻辑范围
fail_wx_bot_login = '200103'
fail_wx_bot_login_desc = u'运维微信登陆失败, 请刷新后重试'

# 非法的客户端(md5 校验不通过，出现此问题，需要立即封锁客户端，!!!此类属于危险操作!!!)
illegal_md5_client = '200200'
illegal_md5_client_desc = u'非法客户端, 警告, 你已被后台跟踪, 注意法律传单!'

# 系统级错误
sys_error = '999999'
sys_error_desc = u'系统错误'