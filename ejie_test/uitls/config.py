#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#测试URL
def test_url():
    url = 'http://postlend.demo.ejie365.cn'
    return url
#邮箱收件人
def post_receiver():
    post_receive = ['95557155@qq.com']
    return post_receive
#用例路径
def case_path():
    # case_paths = r'.\UI_aoto_postlend\others'
    case_paths = r'.\test_case\deduction_claim_managements\deduction_test'
    return case_paths
#日志路径
def log_path():
    log_paths = r'.\logco'
    return log_paths
#截屏照片路径
def picture_path():
    picture_paths = r'.\get_picture'
    return picture_paths
#报告路径
def report_path():
    report_paths = r'.\reports'
    return report_paths
#其他脚本及工具路径
def other_path():
    other_paths = r'.\others'
    return other_paths

