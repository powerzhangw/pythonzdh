#coding=utf-8
from uitls import  unit_star_end
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_01(unit_star_end.Test_define):

    '''百度此页'''
    def test_01_baidu_index(self):
        '''百度测试'''
        self.logs.info_log(u'百度测试')
        self.assertEqual('1','2','success')

    def test_02_baidu_index(self):
        '''百度测试'''
        self.logs.info_log(u'百度测试')
        self.assertEqual('1', '1', 'success')

    def test_03_baidu_index(self):
        '''百度测试'''
        self.logs.info_log(u'百度测试')
        self.assertEqual('1', '1', 'success')
