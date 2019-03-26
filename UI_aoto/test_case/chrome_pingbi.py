# -*- coding: utf-8 -*-
# @Author : "powerzhang"
#屏蔽Chrome的--ignore-certificate-errors提示及禁用扩展插件并实现窗口最大化
from selenium import webdriver
from uitls import kws
import os, traceback

# 创建一个ChromeOptions的对象
option = webdriver.ChromeOptions()
path= r'D:\atest\pythonzdh\lib\chromedriver.exe'
# 去掉提示条的配置
option.add_argument('disable-infobars')
# 获取用目录
try:
    # 异常处理，如果获取到，就使用获取到路径
    userdir = os.environ['USERPROFILE']
except Exception as e:
    # 如果没有获取到，就使用默认的Administrator路径
    # 打印异常信息
    # traceback.print_exc()
    userdir = 'C:\\Users\\Administrator'

userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
userdir = '--user-data-dir=' + userdir
# 添加用户目录
option.add_argument(userdir)
# 设置默认等待时间
driver.implicitly_wait(t)
# 调用谷歌浏览器
driver = webdriver.Chrome(executable_path=path, options=option)
driver.maximize_window()
driver.get("http://riskcontrol.ejie365.cn:8000/#/home")
driver.find_element_by_id("account").send_keys("17621032204")
driver.find_element_by_id("verification").send_keys("EJIE")
driver.find_element_by_id("txtPhoneCertify").send_keys("EJIE")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[7]").click()