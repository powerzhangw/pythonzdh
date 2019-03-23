# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 16:00
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : run.py

import pandas as pd
from class_1106_object.http_request import HttpRequest

#打开Excel获取所有的测试数据
df=pd.read_excel('test_data.xlsx')
test_data=df.values#嵌套列表的数据

#完成HTTP测试
for item in test_data:
    print("目前正在执行的是用例{0}：{1}".format(item[0],item[1]))
    res=HttpRequest.http_request(item[2],eval(item[3]),item[4])
    print('http执行的结果是{0}'.format(res))

#加入单元测试
#框架
#jenkins
#allure



