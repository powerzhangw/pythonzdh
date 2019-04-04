# -*- coding: utf-8 -*-
# import sys
# sys.path.append(r"D:\atest\pythonzdh\UIAutoTest")
import unittest
from uitls.browser import browser
from selenium.webdriver.common.by import By
import lib.logUntil
from uitls.post_result import *
from uitls import post_result
import os




class PostlendTest(unittest.TestCase):

        def setUp(self):
            self.log = lib.logUntil.Log()
            self.po = post_result
            self.browser = browser()
            self.browser.get('http://postlend.demo.ejie365.cn/#/home')
            self.browser.max_window()
            self.browser.input((By.ID,'account'),'17621032204')
            self.browser.input((By.ID,"verification"),'EJIE')
            self.browser.input((By.ID,"txtPhoneCertify"),'EJIE')
            self.browser.click((By.XPATH,'//*[text()=\"登录\"]'))
            log.info("登录成功，开始测试")
            self.browser.implicitly_wait(30)

        def tearDown(self):
            time.sleep(2)
            # if sys.exc_info()[0]:
            for method_name, error in self._outcome.errors:
                if error:
                    case_name = self._testMethodName
                    file_path = os.path.join(os.getcwd() + "/reports/" + case_name + ".png")
                    self.browser.sava_images(file_path)

            self.browser.close()
            self.browser.quit()

if __name__ == '__main__':
    unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(test_test('testfirst002'))
#     suite.addTest(test_test('testfirst003'))
#     unittest.TextTestRunner().run(suite)