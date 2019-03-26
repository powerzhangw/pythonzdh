from selenium import webdriver
from lib.browser import browser
from selenium.webdriver.common.by import By

browser = browser('chrome')
browser.get('http://postlend.demo.ejie365.cn/#/home')
browser.max_window()
browser.input(By.ID,'')
browser.click((By.LINK_TEXT, '新闻'))
browser.wait(5)
browser.quit()
