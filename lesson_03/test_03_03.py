
''''
try:
    a = 3
    b = 0
    print(a / b)
except:

    print('test')
print('con')
'''
from selenium import webdriver
import time
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
driver.implicitly_wait(10)
driver.maximize_window()
try:
    driver.find_element_by_id('notice0').send_keys("上海")
except:
    print('not found element')
driver.find_element_by_id("notice08").send_keys("杭州")