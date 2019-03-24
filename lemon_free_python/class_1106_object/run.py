# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 16:00
# @File    : run.py

import pandas as pd
from lemon_free_python.class_1106_object.http_request import HttpRequest

#打开Excel获取所有的测试数据
df=pd.read_excel('test_data.xlsx')
test_data=df.values#嵌套列表的数据
print(test_data)

# #完成HTTP测试
# for item in test_data:
#     print("目前正在执行的是用例{0}：{1}".format(item[0],item[1]))
#     res=HttpRequest.http_request(item[2],eval(item[3]),item[4])
#     print('http执行的结果是{0}'.format(res))

login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
data = {"mobilephone":"18688773467","pwd":"123456"}
res=HttpRequest.http_request(login_url,data,'GET')
print(res)

#加入单元测试
#框架
#jenkins
#allure



