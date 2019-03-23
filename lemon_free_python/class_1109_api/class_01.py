# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 22:39
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py
import requests
#
# url='http://fm.lemfix.com'
# res_get=requests.get(url)
# print("get请求的结果",res_get)
# print("get请求的状态码",res_get.status_code)
# print("get请求的响应报文",res_get.text)#html json xml
# # print("get请求的响应报文",res_get.json())#确保你返回的数据格式是json
# print("get请求的响应头",res_get.headers)
# # res_post=requests.post(url)
# # print("post请求的结果",res_post)

#登录的地址
login_url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
data={"mobilephone":"18688773467","pwd":"123456"}
#怎么添加请求头 字典的形式添加header里面的字段
headers={"User-Agent":"Mozilla/5.0"}
res_get=requests.get(login_url,data,headers=headers)

print("get请求的结果",res_get)
print("get请求的状态码",res_get.status_code)
print("get请求的text响应报文",res_get.text)#html json xml
print("get请求的json响应报文",res_get.json())#确保你返回的数据格式是json
print("get请求的响应头",res_get.headers)
print("get请求的请求头",res_get.request.headers)

# res_post=requests.post(login_url,data)
# print("post请求的结果",res_post)
# print("post请求的状态码",res_post.status_code)
# print("post请求的text响应报文",res_post.text)#html json xml
# print("post请求的json响应报文",res_post.json())#确保你返回的数据格式是json
# print("post请求的响应头",res_post.headers)