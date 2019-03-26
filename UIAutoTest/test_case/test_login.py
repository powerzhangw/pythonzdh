# -*- coding: utf-8 -*-
# @Author  : powerzhang
import unittest
from lib.browser import browser
from selenium.webdriver.common.by import By

browser = browser('chrome')
browser.get('http://postlend.demo.ejie365.cn/#/home')
browser.max_window()
browser.input((By.ID,'account'),'17621032204')
browser.input((By.ID,"verification"),'EJIE')
browser.input((By.ID,"txtPhoneCertify"),'EJIE')
browser.click((By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div[7]"))


# browser.click((By.LINK_TEXT, '新闻'))
# driver.find_element_by_id("account").send_keys("17621032204")
# driver.find_element_by_id("verification").send_keys("EJIE")
# driver.find_element_by_id("txtPhoneCertify").send_keys("EJIE")
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[7]").click()