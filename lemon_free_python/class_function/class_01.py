# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 19:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py
#字符串 len()

#自定义函数 我们来编写一个函数
#语法：关键字def define
#编写我们的第一个函数
def print_msg():
    '''此函数的作用是完成信息的输出到控制台'''
    print("hello 欢迎大家来听柠檬班的Python课！")
    print("哈哈哈哈哈  Python就是这么厉害")

#调用函数 函数名(传递对应的参数)
# print_msg()
#为什么要写函数？
def add_1():
    print_msg()#调用函数
    print("a+b=",5+6)

def add_2():
    print_msg()#调用函数
    print("a+b=",9+10)

def add_3():
    print_msg()#调用函数
    return("a+b=",-1+-10)

add_1()
add_2()
add_3()

# 写函数的好处：
# 1：代码可以重用
# 2：保持一致性
# 3：可拓展性

# 函数的三个概念：面向对象 面向过程 函数式编程
#面向对象--class 类与对象
#面向过程---def   函数  有return 有返回值
#函数式编程--def  函数  就是函数代码 无返回值

