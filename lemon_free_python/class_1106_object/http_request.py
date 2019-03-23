# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 12:27
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : http_request.py

import requests

class HttpRequest:
    @classmethod
    def http_request(cls,url,data,http_method='POST'):
        if http_method.upper()=='GET':
            res = requests.get(url,data)
        else:#执行的是post请求
            res=requests.post(url,data)
        return res.json()#解析结果

# login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# data = {"mobilephone":"18688773467","pwd":"123456"}
# HttpRequest().http_request(login_url,data,'GET')