# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 22:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py
file=open("sing.txt","w+",encoding='UTF-8')
file.write("我是新加入的summer")
file.seek(10)
print(file.readline())
print(file.readline())
print(file.readline())


