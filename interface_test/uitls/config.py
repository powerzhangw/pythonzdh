#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#邮箱收件人
def post_receiver():
    post_receive = ['907541335@qq.com']
    return post_receive
#报告路径
def report_path():
    report_paths = r'.\reports'
    return report_paths
#用例路径
def case_path():
    case_paths = r'.\test_case'
    return case_paths