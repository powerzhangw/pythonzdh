from classes.class7 import Web
from classes import class7


driver = class7.openbrowser()
driver.get('http://112.74.191.10:8000/')
# 找到这个元素
ele = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
# 再点击这个元素
ele.click()

ele = driver.find_element_by_id('username')
ele.send_keys("13800138006")

ele = driver.find_element_by_css_selector('#password')
ele.send_keys('123456')

ele = driver.find_element_by_xpath('//*[@id="verify_code"]')
ele.send_keys('111111')

ele = driver.find_element_by_css_selector('#loginform > div > div.login_bnt > a')
ele.click()

# web = Web()
# web.openbrowser()
# web.driver.get('http://112.74.191.10:8000/')