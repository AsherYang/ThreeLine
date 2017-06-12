# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pprint

# RR_LOGIN_URL = 'http://www.renren.com/'
MI_LOGIN_URL = 'https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fwww.mi.com%252Findex.html%26sign%3DNDRhYjQwYmNlZTg2ZGJhZjI0MTJjY2ZiMTNiZWExODMwYjkwNzg2ZQ%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180'

class LoginJD():
    def __init__(self):
        self.name = ''
        self.pwd = ''
        self.driver = webdriver.Chrome(r'D:/program_file/python/chromedriver.exe')
        self.driver.get(MI_LOGIN_URL)

    def setLoginInfo(self, username, password):
        self.name = username
        self.pwd = password

    def login(self):
        driver = self.driver
        jdUsername = self.name
        jdPassword = self.pwd
        emailFieldID = "username"
        passFieldID = "pwd"
        loginButtonCs = "#login-button"
        rrLogoCs = "a.logo.ir"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector(loginButtonCs))

        emailFieldElement.clear()
        emailFieldElement.send_keys(jdUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(jdPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector(rrLogoCs))
        print driver.current_url

    def checkGoods(self):
        driver = self.driver
        yuanCs = 'ul.goods-list.rainbow-list.clearfix > li:nth-of-type(1) > a.thumb > img'
        yuanFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_css_selector(yuanCs))
        yuanFieldElement.click()

if __name__ == '__main__':
    login = LoginJD()
    login.setLoginInfo('1181830457@qq.com', '1991429ouyangfan')
    login.login()
    login.checkGoods()
