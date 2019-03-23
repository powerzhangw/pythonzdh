# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 19:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_while.py
#while循环  使某段代码能够重复的执行
# a=9
# while a<10:#FALSE True
#     print("我是while循环")
#死循环

##空数据 空列表 空字符串 空字典 空元组 都是False
# 非空字典 列表 字符串 元组 都是Ture
# while a:
#     print("我是while循环")

#while循环 先判断 再执行  执行完毕再判断  根据结果决定是否继续执行 还是结束循环

#while死循环 怎么去打破  我们可以制作条件 来打破这个死循环
# a=9
# while a>0:#9 8 7 6 5  4 3 2 1
#     print("{0}.我是while循环".format(a))
#     a-=1#每次运行完毕之后 a减去1 a=a-1 8 7 6 5 4 3 2 1 0

#课堂练习：利用while循环来完成1-100的整数相加
a=1
sum=0#sum用来存储结果值
while a<101:#a=1 2
    sum+=a#
    a+=1#2 3
print("1-100的整数和是：{0}".format(sum))
