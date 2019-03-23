# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 10:48
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py
#条件语句有固定的句式和语法
#1.if  条件表达式：
  #满足条件表达式（True）要执行的代码

#2: if 条件表达式：
    #A代码True
    #else:
    #B另外处理的代码 False
# age=6
# if age>=18:#比较运算 True
#     print("已经成年啦！要懂事！")
# else:
#     print("还没有成年，好好学习！")

#3：if...elif...else
# color='9999'
# if color=='red':
#     print("红灯停")
# elif color=='green':
#     print("绿灯行")
# elif color=='yellow':
#     print("黄灯请你等一等")
# else:
#     print("灯的颜色异常，请注意通行安全")

#条件语句;
#1:一组条件语句里面 只有一个if 可以有0个或1个else 可以有0个或多个elif
#2:if  elif  后面 必须加条件表达式 否则会报错
#3：else 后面不能加条件表达式 否则会报错
#4：你可以根据你的不同情况去进行分支划分

#逻辑运算符 成员运算符
# a='hello'
# if 'h'in a:
#     print("h在{0}字符串里面".format(a))
# else:
#     print("h不在{0}字符串里面".format(a))

#逻辑运算符
# a=10
# b=20
# if a>10 and b>10:
#     print("运行结果成立！")
# else:
#     print("运行结果为false")

#非0的数字 就代表 True   0就代表 False
# a=10
# b=0
# if b:
#     print("我是if下面的语句")
# else:
#     print("我是else下面的语句")

#空数据 空列表 空字符串 空字典 空元组 都是false
# 非空字典 列表 字符串 元组 都是Ture
a=''
b='Python'
if b:
    print("我是if下面的语句")
else:
    print("我是else下面的语句")