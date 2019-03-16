from  ddt import  ddt ,data,file_data
import unittest
@ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass
#    @data(2,3)
#    @data([2,4],["a","b"])
    @file_data("D:\\book\\ctrip_19\\lesson_04\\tt.json")
    def test_01(self,tt):
        print(tt)
#        self.assertEqual("selenium","appium")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()