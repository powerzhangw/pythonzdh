# -*- coding: utf-8 -*-
# @Author : "powerzhang"
from selenium import webdriver
import unittest
import time



class Test_define(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # self.driver.get("http://postlend.demo.ejie365.cn/#/home")
        # self.driver.find_element_by_id("account").send_keys("17621032204")
        # self.driver.find_element_by_id("verification").send_keys("EJIE")
        # self.driver.find_element_by_id("txtPhoneCertify").send_keys("EJIE")
        # self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[7]").click()
        # self.logs = log.log_message()
        '''接口进件'''
        # self.get_datas = get_data
        # self.get_datas.get_codes()
        # self.driver = get_element
        # self.browser = self.driver.test_driver('chorome')
        # self.browser.maximize_window()
        # self.browser.get(config.test_url())
        # self.driver.element(self.browser, 'id', public_data.login_input_id).send_keys('17621032204')
        # self.driver.element(self.browser,'id',public_data.verification_input_id).send_keys('EJIE')
        # self.driver.element(self.browser,'id',public_data.txtPhoneCertify_input_id).send_keys('EJIE')
        # self.driver.clic(self.browser,'xpath',public_data.login_clic_xpath)
        # #self.driver.clic(self.browser, 'xpath', public_data.login_clic_xpath)
        # self.browser.implicitly_wait(3)
        print(u'开始执行')

    def tearDown(self):
        time.sleep(2)
        self.browser.quit()
        print(u'执行结束')