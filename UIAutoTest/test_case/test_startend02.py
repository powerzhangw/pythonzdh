# -*- coding: utf-8 -*-
import unittest
from uitls.browser import browser
from selenium.webdriver.common.by import By
from uitls import startend
class Test_01(startend.PostlendTest):
# class test_test(unittest.TestCase):

        def testfirst001(self):
                print("这是02下的运例二条case")
        #
        # def testfirst003(self):
        #         print("这是第003条case")

        # def tearDown(self):
        #     self.browser.close()
        #     print("end!")

# if __name__ == '__main__':
#     unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(test_test('testfirst002'))
#     suite.addTest(test_test('testfirst003'))
#     unittest.TextTestRunner().run(suite)