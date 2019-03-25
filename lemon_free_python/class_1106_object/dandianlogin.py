# -*- coding: utf-8 -*-
# @Author : "powerzhang"
import requests

def qingqiu (url,data,headers,):
    response = requests.request("POST", url, data=data, headers=headers)
    print(response.text)

url = "http://ssonew.demo.ejie365.cn/phoneLogin"
data = "{\"account\":\"17621032204\",\"code\":\"EJIE\",\"captchaCode\":\"EJIE\"}"
headers = {
    'Content-Type': "application/json",
    }
qingqiu(url,data,headers)

# if http_method.upper() == 'GET':
#     res = requests.get(url, data)
# else:  # 执行的是post请求
#     res = requests.post(url, data)
# return res.json()  # 解析结果

# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)