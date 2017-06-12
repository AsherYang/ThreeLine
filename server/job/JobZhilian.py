#! /usr/bin/python
# - * - coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait

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

        userNameFieldElement.clear()
        userNameFieldElement.send_keys(self.name)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(self.pwd)
        loginBtnFieldElement.click()

if __name__ == "__main__":
    zhilian = ZhilianJob()
    zhilian.setLoginInfo('1181830457@qq.com', '1991429ouyangfan')
    zhilian.login()
