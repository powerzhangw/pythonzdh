import  unittest
import HTMLTestRunner

class test_se(unittest.TestCase):
    def setUp(self):
        pass
    def test_01(self):
        self.assertEqual("selenium","selenium")
    def test_02(self):
        self.assertEqual("tim","tim")
    def test_03(self):
        self.assertIn("a","abc")
    def test_04(self):
        self.assertEqual("123", "123")
    def test_05(self):
        self.assertEqual("1234", "124")


    def tearDown(self):
        pass

if __name__ == '__main__':
#    unittest.main()
    suiteTest =unittest.TestSuite()
    suiteTest.addTest(test_se("test_01"))
    suiteTest.addTest(test_se("test_02"))
    suiteTest.addTest(test_se("test_03"))
    suiteTest.addTest(test_se("test_04"))
    suiteTest.addTest(test_se("test_05"))

    filepath=r"D:\atest\pythonzdh\lib\re7.html"
    fp=open(filepath,'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',description="测试报告")
    runner.run(suiteTest)
    fp.close()
