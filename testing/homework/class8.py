# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["noReset"] = "true"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.implicitly_wait(10)
time.sleep(10)
TouchAction(driver).press(x=290, y=154).move_to(x=298, y=402).release().perform()

el1 = driver.find_element_by_xpath(
    "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与廖吴超的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]")
el1.click()
el2 = driver.find_element_by_accessibility_id("美食")
el2.click()

time.sleep(10)
# 断开服务器连接
driver.quit()