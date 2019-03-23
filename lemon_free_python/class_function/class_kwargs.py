# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 18:00
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_kwargs.py
#关键字参数 **kwargs  key word arguments-->字典类型
#参数类型 key value
# def lemon_info(**kwargs):
#     print("kwargs：",kwargs)
#     for item in kwargs.values():
#         print(item)
#
# lemon_info(t_name='华华',t_class='柠檬班',t_course='python全栈自动化')

#结合位置参数 位置参数必须放在关键字参数前
# def lemon_info(age,**kwargs):
#     print("age:",age)
#     print("kwargs：",kwargs)
#     for item in kwargs.values():
#         print(item)
#
# lemon_info(t_name='华华',t_class='柠檬班',t_course='python全栈自动化')

#结合默认值 默认值也必须放在关键字参数前
def lemon_info(age=18,**kwargs):
    print("age:",age)
    print("kwargs：",kwargs)
    for item in kwargs.values():
        print(item)

lemon_info(t_name='华华',t_class='柠檬班',t_course='python全栈自动化')