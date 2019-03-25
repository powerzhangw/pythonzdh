# -*- coding: utf-8 -*-
# @Author  : powerzhang
from class_1106_object.http_request import HttpRequest
login_url = 'ssonew.demo.ejie365.cn/phoneLogin'
data = {"account":"17621032204",
              "code":"EJIE",
              "captchaCode":"EJIE"}
res=HttpRequest.http_request(login_url,data,'POST')
print(res)
