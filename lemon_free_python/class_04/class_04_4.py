# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 14:04
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_04_4.py
#字符串内建函数的应用
str_1='666HELLO666le@mon666'
#5.字符串的头和尾的处理 strip()
res=str_1.strip('6')
print('处理之后的结果:{}'.format(res))

#4.字符串的切片 split()  可以指定切割次数
# res=str_1.split('@',1)#切割之后会返回列表类型的数据，里面的元素还是字符串
# print('切割之后的结果:{}'.format(res))

#3.字符串的替换 replace()
# res=str_1.replace('L','@')#你要替换的目标字符/字符串   你传递的新值
# print('替换之后的结果:{}'.format(res))

#2.查找子字符串
# res=str_1.find('a')
# print('查找结果:{}'.format(res))
#单个字符  如果可以在字符串里面找到 就会返回对应的索引值
#子字符串 如果可以找到子字符串 会返回子字符串的第一个元素在原来字符串所在的索引
#如果找不到  就会返回-1

#1.改变大小写的内建函数  upper()  lower()
# new_str=str_1.upper()
# new_str=str_1.lower()
# print('新字符串:{}'.format(new_str))