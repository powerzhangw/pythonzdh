#_*_coding:utf-8_*_
import  time,unittest,HTMLTestRunner
from lesson_07.loginPage import loginPage
from lesson_07.searchPage import searchPage
from  lesson_07.noPage import noPage
from  lesson_07.detailPage import detailPage
from selenium import  webdriver


class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('tt')
        path = r'D:\atest\pythonzdh\lib\chromedriver.exe'
        cls.driver = webdriver.Chrome(path)
        cls.driver.get('https://passport.ctrip.com/user/login?')
        cls.driver.maximize_window()

    def test_01(self):
        lo=loginPage(self.driver)
        l=lo.LoginIn("","")

        print(l)
        self.assertIn("my",l)
    def test_02(self):
        self.driver.get("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        s=searchPage(self.driver)
        s.Search_Train("杭州","上海","20190105")

    def test_03(self):
        n= noPage(self.driver)
        n.bookBtn()

    def test_04(self):
        d = detailPage(self.driver)
        d.detail_name("小王")

    def tearDownClass(cls):

       cls.driver.quit()


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(logingTest("test_01"))
    filepath = r"D:\atest\pythonzdh\lib\re.html"
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description="测试报告")
    runner.run(suiteTest)
    fp.close()

