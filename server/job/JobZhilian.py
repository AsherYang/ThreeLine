#! /usr/bin/python
# - * - coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

"""
Author: AsherYang
Email:  1181830457@qq.com
Date:   2017/5/23
Desc:   智联招聘类
"""
ZHILIAN_HOST_URL = 'https://www.zhaopin.com/'

class ZhilianJob():

    def __init__(self):
        self.driver = webdriver.Chrome(r'D:/program_file/python/chromedriver.exe')
        self.driver.get(ZHILIAN_HOST_URL)
        self.name = ''
        self.pwd = ''

    def setLoginInfo(self, name, password):
        self.name = name
        self.pwd = password

    def login(self):
        driver = self.driver
        userNameFieldCssSelect = '#loginname'
        passwordFieldCssSelect = '#password'
        loginBtnFieldCssSelect = 'div.logbtn > button'

        userNameFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_elements_by_css_selector(userNameFieldCssSelect))
        passwordFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_elements_by_css_selector(passwordFieldCssSelect))
        loginBtnFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_elements_by_css_selector(loginBtnFieldCssSelect))

        # print type(userNameFieldElement)
        # userNameFieldElement passwordFieldCssSelect is a list in zhilian(tab)
        userNameFieldElement[0].clear()
        userNameFieldElement[0].send_keys(self.name)
        passwordFieldElement[0].clear()
        passwordFieldElement[0].send_keys(self.pwd)
        loginBtnFieldElement[0].click()

        logoCssSelect = 'div.nav_img.fl > img'
        WebDriverWait(driver, 10).until(lambda driver : driver.find_elements_by_css_selector(logoCssSelect))
        refreshCssSelect = 'div.zhImgCole > div.myLink > a.myLinkA.linkRefresh > i'
        refreshFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_elements_by_css_selector(refreshCssSelect))
        refreshFieldElement[0].click()

        time.sleep(5)
        driver.close()
        driver.quit()

if __name__ == "__main__":
    zhilian = ZhilianJob()
    zhilian.setLoginInfo('oyf1991@126.com', '1991429ouyangfan')
    zhilian.login()
