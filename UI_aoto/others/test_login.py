# -*- coding: utf-8 -*-
# @Author  : powerzhang
from selenium import webdriver
path= r'D:\atest\pythonzdh\lib\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("http://postlend.demo.ejie365.cn/#/home")
driver.find_element_by_id("account").send_keys("17621032204")
driver.find_element_by_id("verification").send_keys("EJIE")
driver.find_element_by_id("txtPhoneCertify").send_keys("EJIE")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[7]").click()