import  unittest
import HTMLTestRunner

class test_se(unittest.TestCase):
    def setUp(self):
        pass
    def test_01(self):
        self.assertEqual("selenium","appium")
    def test_02(self):
        self.assertEqual("tim","tim")
    def test_03(self):
        self.assertIn("a","abc")

    def tearDown(self):
        pass

if __name__ == '__main__':
#    unittest.main()
    suiteTest =unittest.TestSuite()
    suiteTest.addTest(test_se("test_01"))
    suiteTest.addTest(test_se("test_02"))
    suiteTest.addTest(test_se("test_03"))
    filepath="C:\\re.html"
    fp=open(filepath,'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',description="测试报告")
    runner.run(suiteTest)
    fp.close()
