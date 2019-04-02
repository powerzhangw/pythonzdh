# -*- coding: utf-8 -*-
# import sys
# sys.path.append(r"D:\atest\pythonzdh\UIAutoTest")
import unittest
from uitls.browser import browser
from selenium.webdriver.common.by import By
import lib.logUntil
log = lib.logUntil.Log()
class PostlendTest(unittest.TestCase):
        def setUp(self):
            self.browser = browser()
            self.browser.get('http://postlend.demo.ejie365.cn/#/home')
            self.browser.max_window()
            self.browser.input((By.ID,'account'),'18208185860')
            self.browser.input((By.ID,"verification"),'EJIE')
            self.browser.input((By.ID,"txtPhoneCertify"),'EJIE')
            self.browser.click((By.XPATH,'//*[text()=\"登录\"]'))
            self.browser.wait(5)
            log.info("登录成功，开始测试")
            print("start!")
        def test001(self):
            # 点击客户管理
            self.browser.click((By.ID, 'tTopMenucustomer'))
            # 点击在贷客户
            self.browser.click((By.XPATH, '//*[@id="tSideMenuloanList"]/span'))
            #搜索借款人
            self.browser.input((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input'),'周杰伦')
            self.browser.click((By.XPATH,'//*[text()=\"筛选\"]'))


        # def tearDown(self):
        #     self.browser.wait(5)
        #     self.browser.close()
        #     print("end!")
if __name__ == '__main__':
    unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(test_test('testfirst002'))
#     suite.addTest(test_test('testfirst003'))
#     unittest.TextTestRunner().run(suite)