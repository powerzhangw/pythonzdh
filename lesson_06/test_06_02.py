from ddt import  ddt,data,file_data
import  unittest

@ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass

#    @data(2,3)
#    @data(["se","app"],["appium","tim"])
    @file_data("D:\\book\\ctrip_19\\lesson_04\\tt.json")
    def test_01(self,tt):
        print(tt)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()