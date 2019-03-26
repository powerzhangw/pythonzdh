# coding:utf-8
import unittest
import os,time
from uitls.HTMLTestRunner_cn import HTMLTestRunner

# 用例路径
case_path = os.path.join(os.getcwd(), "test_case")
# case_path = os.path.join(os.getcwd(), "demo")

# 报告存放路径
report_path = os.path.join(os.getcwd(), "reports")
#格式化当前日期
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# html报告文件
report_abspath = os.path.join(report_path, now+"result.html")

discover = unittest.defaultTestLoader.discover(case_path,
                                            pattern="test*.py",
                                            top_level_dir=None)

fp = open(report_abspath, "wb")
runner = HTMLTestRunner(stream=fp,
                        verbosity=2,
                        title=u'自动化测试报告,测试结果如下：',
                        description=u'用例执行情况：')

# 调用add_case函数返回值
runner.run(discover)
fp.close()
