#coding=utf-8
import unittest
from uitls import get_element
from uitls import log
from uitls import config
from common import public_data
from uitls import get_data
import time
import sys #


class Test_define(unittest.TestCase):

    def setUp(self):
        self.logs = log.log_message()
        self.get_datas = get_data
        self.get_datas.get_codes()
        self.driver = get_element
        self.browser = self.driver.test_driver('chrome')
        self.browser.maximize_window()
        self.browser.get(config.test_url())
        self.driver.element(self.browser, 'id', public_data.login_input_id).send_keys('17621032204')
        #self.driver.element(self.browser,'id',public_data.psssword_input_id).send_keys('446544')
        self.driver.element(self.browser,'id',public_data.verification_input_id).send_keys('EJIE')
        self.driver.element(self.browser,'id',public_data.txtPhoneCertify_input_id).send_keys('EJIE')
        self.driver.clic(self.browser,'xpath',public_data.login_clic_xpath)
        #self.driver.clic(self.browser, 'xpath', public_data.login_clic_xpath)
        self.browser.implicitly_wait(3)
        print(u'开始执行')

    def tearDown(self):
        time.sleep(2)
        self.browser.quit()
        print(u'执行结束')