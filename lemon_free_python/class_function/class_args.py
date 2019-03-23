# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_args.py
#不定长参数 /动态参数 *变量名   *args  arguments --args 按照这个规范
#把这个数据 转成了元组形式
# def add(*args):
#     print(args)
#     print("args的类型：",type(args))
#     count=0
#     for item in args:
#         count+=item
#     return count
#
# result=add(1,2,3,4,5,6,7,9,10,11,23,19)
# print("动态参数的求和结果",result)
#1:什么时候用这个动态参数-->当你不确定参数的个数的时候 就可以用动态参数

#2:位置参数和动态参数的结合使用  位置参数放在动态参数前
# def greet(content,*args):#TypeError: greet() missing 1 required keyword-only argument: 'content'
#     name=''
#     for item in args:
#         name+=item
#         name+='、'
#     print(name,content)
# greet("早上好","华华","小简","毛毛")

#3:默认参数和动态参数的结合使用  如果你要让你的默认值生效 请放到动态参数的后面（放前面 就不生效）
def greet(*args,content='晚上好'):
    name=''
    for item in args:
        name+=item
        name+='、'
    print(name,content)
greet("华华","小简","毛毛")