from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://postlend.demo.ejie365.cn/#/home")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()