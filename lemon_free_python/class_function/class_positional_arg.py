# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 14:13
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_positional_arg.py
#函数里面的位置参数  添加参数  参数化
def print_msg(a,b):#位置参数/形参
    '''此函数的作用是完成信息的输出到控制台'''
    # print("我谁都不用")
    print("a参数的值",a)
    print("b参数的值",b)

# print_msg("a:hello","b:python")#实参
# print_msg(b="a:hello",a="b:python")
# print_msg("同学你好呀","柠檬班的Python课怎么样呀？")
# print_msg()

#如果是位置参数
#1：有几个位置参数 咱们就要传递几个参数 不能多不能少
#少了：print_msg() missing 1 required positional argument: 'b'
#多了：TypeError: print_msg() takes 2 positional arguments but 3 were given
#2:按顺序赋值  常规的用法
#3:传递的参数 使用顺序 他不一定是按照顺序
#4：参数一定都会使用
#5:可以不按顺序赋值，通过关键字指明  通过形参的指定去赋值

#小练习
#利用for循环  range函数 编写任意整数序列的求和函数
def add(m,n,k):
    count=0
    for i in range(m,n,k):
        count+=i
    # print("函数内部打印求和结果是：",count)
    return count

result=add(0,101,2)
print("结果值是：",result)

#三步函数法
# 1.先用零散的代码写出功能要求
# 2.变成函数 def 函数名()
# 3.想办法提高他的复用性 参数化