# -*- coding: UTF-8 -*-
from classes import class7
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = class7.openbrowser()
driver.maximize_window()
driver.get('http://112.74.191.10:8000/')
# 找到这个元素
ele = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
# 再点击这个元素
ele.click()

# 登录
ele = driver.find_element_by_id('username')
ele.send_keys("13800138006")

ele = driver.find_element_by_css_selector('#password')
ele.send_keys('123456')

ele = driver.find_element_by_xpath('//*[@id="verify_code"]')
ele.send_keys('111111')

ele = driver.find_element_by_css_selector('#loginform > div > div.login_bnt > a')
ele.click()

#搜索
ele = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a')
ele.click()

ele = driver.find_element_by_xpath('//*[@id="q"]')
ele.send_keys('手机')

ele = driver.find_element_by_xpath('//*[@id="searchForm"]/button')
ele.click()

#移动到元素
ele = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li[10]/div/div[5]/div[2]/a')
actions = ActionChains(driver)
actions.move_to_element(ele).perform()
#点加购物车
ele.click()

#切换iframe
ele = driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
driver.switch_to.frame(ele)

ele = driver.find_element_by_xpath('//*[@id="addCartBox"]/div[1]/div/span')
print(ele.text)

#切出iframe
driver.switch_to.default_content()
ele = driver.find_element_by_xpath('//*[@id="layui-layer1"]/span/a')
ele.click()

#滚回购物车按钮
ele = driver.find_element_by_xpath('//*[@id="hd-my-cart"]/a/div')
actions.move_to_element(ele).perform()
ele.click()

ele = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/a')
ele.click()
time.sleep(2)
ele = driver.find_element_by_xpath('/html/body/div[14]/div/button')
# actions.move_to_element(ele).perform()
ele.click()

ele = driver.find_element_by_xpath('//*[@id="cart4_form"]/div/div/dl/dd/div/div[2]/ul/li[2]/div')
ele.click()

# 点击退出登录
driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[1]/a').click()

# 切换窗口
handles = driver.window_handles
# 关闭当前在操作的页面
driver.close()
# 根据界面handle的标识切换
driver.switch_to.window(handles[1])
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/a[2]').click()
