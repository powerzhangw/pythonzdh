# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 15:34
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_default_arg.py
#默认参数
def greet(name,content='吃早饭了没？'):#content有默认值
    '''函数的用处是向不同的用户 发问候'''
    print(name+content)

# greet("华华","下午好！")
# greet("同学们，")
greet(content='hello',name="正在听课的同学们")
#默认参数
#1：带有默认值的参数 必须放在位置参数后面 SyntaxError: non-default argument follows default argument
#2:默认参数可以有多个 在遵守条件1的前提下
#3：如果有默认值  这个参数 可以不传值 不传值 就取默认值 传值 就以你的值为准
#4：按顺序赋值 也可以通过关键字指定来赋值
