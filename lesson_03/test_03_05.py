from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.baidu.com")
driver.find_element(By.ID,"kw").send_keys("test")
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
