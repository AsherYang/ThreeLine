#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/6/29
Desc:   产生6位随机短信验证码类
"""

import random


class RandomPwd:
    def __init__(self):
        pass

    def genPwd(self):
        a_list = []
        while len(a_list) < 6:
            x = random.randint(0, 9)
            # if x not in s:
            a_list.append(x)
        print a_list
        string = ''.join(list(map(str, a_list)))
        return string


if __name__ == '__main__':
    randomPwd = RandomPwd()
    print randomPwd.genPwd()
