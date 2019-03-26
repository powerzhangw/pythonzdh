from selenium import webdriver
import unittest
import time
from uitls import  log

class MyTest(unittest.TestCase):
    def setUp(self):
        self.logs = log.log_message()
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
        print("测试开始")

    def test_baidu(self):
        self.logs = log.log_message()
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title=driver.title
        self.assertEquals(title,"unittest_百度搜索")

    def tearDown(self):
        self.logs = log.log_message()
        self.driver.quit()
        print("测试结束")

if __name__=="__main__":
    unittest.main()