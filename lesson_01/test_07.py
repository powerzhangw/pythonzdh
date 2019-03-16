from selenium import webdriver
from selenium.webdriver.support.select import  Select
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome(path)
driver.get('https://mail.qq.com/cgi-bin/loginpage')
time.sleep(6)
driver.find_element_by_id('composebtn').click()
driver.switch_to.frame('mainFrame')
time.sleep(2)
driver.find_element_by_name('UploadFile').send_keys('D:\\web\\test.txt')