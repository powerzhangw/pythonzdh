#_*_coding:utf-8_*_
import  time,unittest
from lesson_07.loginPage import loginPage
from lesson_07.searchPage import searchPage
from selenium import  webdriver
class logingTest(unittest.TestCase):
    def setUp(self):
        print('tt')
        path = 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.driver.get('https://passport.ctrip.com/user/login?')
        self.driver.maximize_window()

    def test_01(self):
        lo=loginPage(self.driver)
        l=lo.LoginIn("E530104548","t123456@")

        print(l)

    def test_02(self):
        self.driver.get("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        s=searchPage(self.driver)
        s.Search_Train("杭州","上海","20190105")

    def tearDown(self):
        pass
   #     self.driver.quit()

if __name__ == '__main__':
    unittest.main()
