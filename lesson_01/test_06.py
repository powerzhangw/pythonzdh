from selenium import webdriver
from selenium.webdriver.support.select import  Select
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome(path)
driver.get('https://www.baidu.com/')
ActionChains(driver).move_to_element(driver.find_element_by_link_text("设置")).perform()
time.sleep(2)
driver.find_element_by_class_name('setpref').click()
time.sleep(2)
r = driver.find_elements_by_name("SL")
print(r)
print(len(r))
r.pop(1).click()