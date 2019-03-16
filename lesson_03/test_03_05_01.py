
import time
from lesson_03.com import driver
from lesson_03.search_page import  search


driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
driver.maximize_window()
'''
id('notice01').send_keys("上海")
id('notice08').send_keys("杭州")
js("dateObj")
id("dateObj").clear()
id("dateObj").send_keys("2019-01-05")
'''
search("notice01","#notice08","dateObj")