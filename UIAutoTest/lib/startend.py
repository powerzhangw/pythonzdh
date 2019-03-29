# -*- coding: utf-8 -*-
# import sys
# sys.path.append(r"D:\atest\pythonzdh\UIAutoTest")
import unittest
from uitls.browser import browser
from selenium.webdriver.common.by import By

class PostlendTest(unittest.TestCase):
        def setUp(self):
            self.browser = browser('chrome')
            self.browser.get('http://postlend.demo.ejie365.cn/#/home')
            self.browser.max_window()
            self.browser.input((By.ID,'account'),'17621032204')
            self.browser.input((By.ID,"verification"),'EJIE')
            self.browser.input((By.ID,"txtPhoneCertify"),'EJIE')
            self.browser.click((By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div[7]"))

            print("start!")

        # def testfirst002(self):
        #         print("这是第0二条case")
        #
        # def testfirst003(self):
        #         print("这是第003条case")

        def tearDown(self):
            self.browser.close()
            print("end!")

# if __name__ == '__main__':
#     unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(test_test('testfirst002'))
#     suite.addTest(test_test('testfirst003'))
#     unittest.TextTestRunner().run(suite)