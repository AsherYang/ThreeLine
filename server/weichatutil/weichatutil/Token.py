#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2017/6/11
Desc:   token create
"""
# d9218b046dde43147ea6c889ea67ede8437ff696
import hashlib
import os

print hashlib.sha1(os.urandom(24)).hexdigest()