from selenium import webdriver
import time
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
driver.maximize_window()
driver.find_element_by_id('notice01').send_keys("上海")
driver.find_element_by_id("notice08").send_keys("杭州")

driver.find_element_by_id("searchbtn").click()
time.sleep(3)
driver.find_element_by_css_selector("#tbody-01-K18050 > div.railway_list > div.w6 > div:nth-child(1) > a").click()
time.sleep(2)
driver.find_element_by_css_selector("#appd_wrap_close").click()
time.sleep(2)
driver.find_element_by_css_selector("#btn_nologin").click()
time.sleep(2)
driver.find_element_by_css_selector("#pasglistdiv > div > ul > li:nth-child(2) > input").send_keys("小王")
