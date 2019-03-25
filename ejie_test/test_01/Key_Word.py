# -*- coding: utf-8 -*-
# @Author : "powerzhang"
from selenium import webdriver
from selenium.webdriver.common.by import By
path = r'D:\atest\pythonzdh\lib\chromedriver.exe'
driver = webdriver.Chrome(path)

class KeyWord:

    @classmethod
    def inputvalue (self,xpath,value):
        self.driver.findElement(By.xpath(xpath)).clear()
        self.driver.findElement(By.xpath(xpath)).sendKeys(value)

    # @classmethod
    def geturl(self,url):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        path = r'D:\atest\pythonzdh\lib\chromedriver.exe'
        driver = webdriver.Chrome(path)
        self.driver.get(url)
        driver.maximize_window()

    @classmethod
    def click(cls,xpath):
        driver.findElement(By.xpath(xpath)).click()

    @classmethod
    def submit(cls,xpath):
        driver.findElement(By.xpath(xpath)).submit()

    geturl().geturl("http://riskcontrol.ejie365.cn:8000/#/home")

# inputvalue('//*[@id="account"]',"17621032204")
# inputvalue('//*[@id="verification"]','EJIE')
# inputvalue('//*[@id="txtPhoneCertify"]','EJIE')
# click("/html/body/div/div/div[2]/div/div[2]/div[7]")

geturl

