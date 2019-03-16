from selenium import webdriver
from selenium.webdriver.support.select import  Select
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
from selenium.webdriver.common.action_chains import ActionChains
import  time
from PIL import Image
driver = webdriver.Chrome(path)
driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')

#driver.find_element_by_id("dateObj").send_keys("2019-01-12")
#driver.execute_script("document.getElementById('dateObj').value=2019-01-12")
driver.execute_script("document.getElementById('dateObj').removeAttribute('readonly')")
driver.find_element_by_id("dateObj").clear()
driver.find_element_by_id("dateObj").send_keys("2019-01-05")
time.sleep(5)