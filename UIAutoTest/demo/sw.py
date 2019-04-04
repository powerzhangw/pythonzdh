# -*- coding: utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys(u'梦雨情殇')  #搜索“梦雨情殇的博客”
now_handle = driver.current_window_handle   #获取当前窗口的句柄
print(now_handle)  #打印当前窗口的句柄
print(driver.title)  #获取打开页面的标题
driver.find_element_by_id('su').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()  #点击第一条查询的数据
all_handles = driver.window_handles   #获取到当前所有的句柄,所有的句柄存放在列表当中
print(all_handles)  #打印句柄
'''获取非最初打开页面的句柄'''
for handles in all_handles:
    if now_handle != handles:
        driver.switch_to_window(handles)
print(driver.title)  #获取切换后的标题
time.sleep(3)
driver.quit()