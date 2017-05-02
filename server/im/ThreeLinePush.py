#!/usr/bin/python
# - * - coding: utf-8 - * -

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/05/01
Desc:   threeline use jpush
http://blog.csdn.net/mmmwhy/article/details/62887479
"""

import jpush as jpush
from conf import app_key, master_secret
from jpush import common

_jpush = jpush.JPush(app_key, master_secret)
push = _jpush.create_push()

# set debug logging
_jpush.set_logging("DEBUG")
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello asher yang congratulation !")
push.platform = jpush.all_
try:
    response = push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("APIConnectionException")
except common.JPushFailure:
    print "JPushFailure"
except:
    print "jpush send fail"
