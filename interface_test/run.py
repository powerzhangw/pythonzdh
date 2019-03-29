#coding=utf-8
import unittest
import time
from uitls import config
from uitls import post_email
from uitls import HTMLTestRunner
from uitls import delete_report
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#组织测试用例
case_path = config.case_path()
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
#格式化当前日期
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
# 打开一个文件，将result写入此file中
reportpath = config.report_path()


if __name__ == '__main__':
    delete_report.dell_oldreport()
    with open(reportpath+ r"\result" + now + '.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f, title='test result', description='1111111111', verbosity=2)
        runner.run(discover)
    #post_email.post_email()