#coding=utf-8
import config
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def dell_oldreport():
    path_name = config.report_path()
    pathname = []

    for (dirpath, dirnames, filenames) in os.walk(path_name):
        for filename in filenames:
            pathname.append(os.path.join(dirpath, filename))
    for path in pathname:
        if os.path.exists(path):
            if 'html'in path:
                os.remove(path)