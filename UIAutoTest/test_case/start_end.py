# -*- coding: utf-8 -*-
# coding:utf-8
import unittest

class Test1(unittest.TestCase):
    def setUp(self):
        browser = browser()
        self.browser.get('http://postlend.demo.ejie365.cn/#/home')
        self.browser.max_window()
        self.browser.input((By.ID,'account'),'17621032204')
        self.browser.input((By.ID,"verification"),'EJIE')
        self.browser.input((By.ID,"txtPhoneCertify"),'EJIE')
        self.browser.click((By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div[7]"))
        print("start!")

    def tearDown(self):
        self.browser.quit()
        print("end!")

if __name__ == "__main__":
    unittest.main()