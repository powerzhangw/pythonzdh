import  unittest
import HTMLTestRunner
from lesson_03.com import driver,read_excel
from lesson_06.search_page import  search
#参数与脚本分离 ，数据驱动
class test_se(unittest.TestCase):
    def setUp(self):
      self.data=read_excel("testdata.xlsx",0)[0]

    def test_01(self):
        print(self.data)
        driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
        driver.maximize_window()
        search("notice01", "#notice08", "dateObj")
        self.assertIn("SearchTrain.aspx",driver.current_url)


    def tearDown(self):
        pass

if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(test_se("test_01"))
    filepath = "C:\\re.html"
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description="测试报告")
    runner.run(suiteTest)
    fp.close()
