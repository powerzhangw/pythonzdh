#coding=utf-8
import unittest
import time
from uitls import config
# from uitls import post_email
from uitls import HTMLTestRunner_jpg
# from uitls import delete_report

#组织测试用例
case_path = config.case_path()
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)

# discover 筛选出的测试用例，循环添加到测试条件中
# for test_suite in discover:
#     for test_case in test_suite:
#         test_suite .addTests(test_case)
#         print(test_suite)

# testunit.addTests(discover)#直接加载discover
#格式化当前日期
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 打开一个文件，将result写入此file中 将测试报告写入reports
reportpath = config.report_path()


if __name__ == '__main__':
    # delete_report.dell_oldreport()
    with open(reportpath+ r"\result" + now + '.html', 'wb') as f:
        runner = HTMLTestRunner_jpg.HTMLTestRunner(
            stream=f, title='贷后自动化测试报告', description='测试详细情况如下表格', verbosity=2)
        runner.run(discover)
    #post_email.post_email()