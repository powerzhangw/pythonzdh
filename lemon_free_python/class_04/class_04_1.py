# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 17:01
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_04_1.py
#Python常用数据类型之一 字符串
#成对的双引号 或者是成对的单引号括起来的内容 就是字符串
a='lemon'
b="lemon best"
#type
# print(type(a))
# c='1'
# print(type(c))

#字符串的取值访问
#字符串：字符串里面的元素是由一个一个的字符组成
#字符串都是有索引 从0开始数的
#字符串的取值方式 字符串名[索引值]
# print(a[3])
# print(a[4])

#反序访问  从数据的尾巴开始定义索引 从-1开始
#取最后一个值
# print(a[4])
# print(a[-1])

#怎么处理字符串里面的特殊字符  转义 加r/R  加\
#\n  \t \r
# a=r'python\tlemon'
# print(a)

#字符串的运算： + *
#+ 是拼接字符串的意思
# a='柠檬班'
# b='is best'
# c=a+b
# print(type(c))

#*重复字符串输出
# print(a*5)

#判断字符串in not in 成员运算符 返回值 布尔值 True False
# a='hello'
# print('t' in a)

#如果是不同的类型的数据拼接 怎么办？
a=666
b='hello'
print(str(a)+b)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'