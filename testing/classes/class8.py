# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 登录
el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el1.send_keys("3599292078")
# driver.find_element_by_accessibility_id("密码 安全").clear()
el2 = driver.find_element_by_accessibility_id("密码 安全")
el2.clear()
el2.send_keys("xiaobao168")
el3 = driver.find_element_by_accessibility_id("登录")
el3.click()

# 登出
el4 = driver.find_element_by_accessibility_id("帐户及设置")
el4.click()
el5 = driver.find_element_by_accessibility_id("设置")
el5.click()
el6 = driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
el6.click()
el7 = driver.find_element_by_accessibility_id("退出当前帐号按钮")
el7.click()
el8 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
el8.click()

driver.quit()
