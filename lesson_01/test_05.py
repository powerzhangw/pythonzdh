from selenium import webdriver
from selenium.webdriver.support.select import  Select
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome(path)
driver.get('https://mail.qq.com/cgi-bin/loginpage')

driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('1234')
time.sleep(2)
driver.switch_to.default_content()
driver.find_element_by_link_text('基本版').click()
