# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 22:40
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_for_range.py
#range(m,n,k) # m 开头 n 结尾  k步长 取头不取尾
#作用的  生成一个整数序列
# print(list(range(0,5,2)))#0 2 4
# print(list(range(0,10,3)))#0 3 6 9
#k的值默认为1 k=1
# print(list(range(2,6)))# 2 3
#只传一个值n  开头默认为0 k默认为1
# print(list(range(6)))# 0 1 2 3 4 5
# s='hello'
# print(s[0:5:2])#0 2 4
#小题目：利用for循环 完成1-100的整数和相加
# count=0
# for item in range(1,101):#1 2 3 4 5...100
#    count+=item
# print("最后的结果值是{0}".format(count))
#利用range for 完成某个列表的倒序输出
s=[1,2,3,4,5,6,7]#0 1 2 3 4 5 6
for i in range(6,-1,-1):#6 0 -1  6 5 4 3 2 1 0
    print(s[i])