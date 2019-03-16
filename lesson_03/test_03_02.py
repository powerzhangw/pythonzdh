from selenium import webdriver
import time
from lesson_03.com import id,js

path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
driver.maximize_window()

id(driver,'notice01').send_keys("上海")
id(driver,'notice08').send_keys("杭州")
js(driver,"dateObj")
id(driver,"dateObj").clear()
id(driver,"dateObj").send_keys("2019-01-05")


