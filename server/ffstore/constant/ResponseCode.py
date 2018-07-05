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

# ---------------------------------------------------------- 通用类返回码
# 操作成功
op_success = '000001'
op_success_desc = u'successfully'

# 操作失败
op_fail = '000002'
op_fail_desc = u'操作失败'

# 传递参数异常
fail_api_args = '000100'
fail_api_args_desc = u'参数错误'

# 数据库操作失败
fail_op_db_data = '000101'
fail_op_db_data_desc = u'数据操作失败'

# ---------------------------------------------------------- API类返回码

# 无效用户电话号码
invalid_user_phone = '200001'
invalid_user_phone_desc = u'用户电话号码无效'

# 无效用户地址
invalid_user_address = '200002'
invalid_user_address_desc = u'用户地址无效'

# 更新用户信息出错
fail_update_user_info = '200010'
fail_update_user_info_desc = u'更新信息失败'

# 记录用户消费失败
fail_add_user_cost = '200020'
fail_add_user_cost_desc = u'记录用户消费失败'

# 获取微信session_key 无效
fail_wx_session_key = '200100'
fail_wx_session_key_desc = u'微信鉴权失败'

# 前台小程序(API), md5 校验失败，统一返回给用户操作失败的提示。
fail_check_api_md5 = '200111'
fail_check_api_md5_desc = u'操作失败'

# 这里的用户是指前台(小程序) 用户
success_user_login = '200112'
success_user_login_desc = u'登录成功!'

fail_cate_not_found = '200113'
fail_cate_not_found_desc = u'未找到对应的商品分类'

fail_goods_not_found = '200114'
fail_goods_not_found_desc = u'未找到对应的商品'

# ---------------------------------------------------------- 后台类返回码

# 后台用户统一使用admin表示，指明是后天管理员
# 管理员权限校验成功
success_check_admin_permission = '200150'
success_check_admin_permission_desc = u'管理员权限校验通过'

fail_admin_login = '200151'
fail_admin_login_desc = u'用户名或者密码错误'

fail_admin_out_of_date = '200152'
fail_admin_out_of_date_desc = u'登陆已过期'

# 非法的客户端(md5 校验不通过，出现此问题，需要立即封锁客户端，!!!此类属于危险操作!!!)
illegal_md5_client = '200200'
illegal_md5_client_desc = u'非法客户端, 警告, 你已被后台跟踪, 注意法律传单!'

# 运维微信登陆失败, 请刷新后重试。关于运维微信与其他状态码并不在同一逻辑范围
fail_wx_bot_login = '200500'
fail_wx_bot_login_desc = u'运维微信登陆失败, 请刷新后重试'

# ---------------------------------------------------------- 系统级返回码
# 系统级错误
sys_error = '999999'
sys_error_desc = u'系统错误'