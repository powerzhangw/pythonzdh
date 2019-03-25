# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 12:13
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : http_request.py

import requests

def http_request(url,data,http_method='POST'):
    if http_method.upper()=='GET':
        res = requests.get(url,data)
    else:#执行的是post请求
        res=requests.post(url,data)
    print("http请求的json响应报文",res.json())

# login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# data = {"mobilephone":"18688773467","pwd":"123456"}
# http_request(login_url,data,'GET')

login_url = 'ssonew.demo.ejie365.cn/phoneLogin'
data = {"account":"17621032204",
              "code":"EJIE",
              "captchaCode":"EJIE"}
http_request(login_url,data)
