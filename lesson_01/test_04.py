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
#driver.find_element_by_css_selector('#nr > option:nth-child(2)').click()
#Select(driver.find_element_by_name('NR')).select_by_index(2)
#Select(driver.find_element_by_name('NR')).select_by_value('20')
#Select(driver.find_element_by_name('NR')).select_by_visible_text('每页显示20条')
print(Select(driver.find_element_by_name('NR')).options)