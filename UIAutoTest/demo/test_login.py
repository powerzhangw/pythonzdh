# -*- coding: utf-8 -*-
import unittest
from lib.browser import browser
from selenium.webdriver.common.by import By
browser = browser('chrome')
browser.get("https://www.baidu.com/")
browser.input((By.ID,"kw"),"selenium")
browser.click((By.ID,"su"))





















































# browser = browser('chrome')
# browser.get('http://postlend.demo.ejie365.cn/#/home')
# browser.max_window()
# browser.input((By.ID,'account'),'17621032204')
# browser.input((By.ID,"verification"),'EJIE')
# browser.input((By.ID,"txtPhoneCertify"),'EJIE')
# browser.click((By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div[7]"))