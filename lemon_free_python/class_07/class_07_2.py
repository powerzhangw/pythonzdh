# -*- coding: utf-8 -*-
# @Time    : 2018/10/7 10:33
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_07_2.py
# a={'name':'华华','age':18,'money':99.99,'score':[100,100,80]}
#增删改查
#增加元素  如果key不存在  那么就是添加一个新值
# a["class"]="柠檬班"
# print("修改之后的字典值:{0}".format(a))

#修改元素 如果key存在  那么就是修改key对应的值
# a['name']='柠檬班华华'
# print("修改之后的字典值:{0}".format(a))

#查询,字典的取值  字典名[key]
# print("字典里面的姓名是：{0}".format(a['name']))

#删除 字典是无序的  只能根据key去做删除  字典名.pop(key)
# a.pop('age')
# print("删除操作之后的字典值:{0}".format(a))

#拓展方法：
# a.clear()#清空字典

# del a['money']# del 字典名[key]  删除指定key的元素

# a.popitem()#随机删除一组数据
#取值的一些方法
# print(a.keys())
# print(a.values())
# print(a.items())

#a.update(c) c里面的key如在a里面存在，那么就会把c的value值更新到a里面去  如果不存在
#那么就把不存在的key-value 添加到a里面去
a={'name':'华华','age':18,'money':99.99,'score':[100,100,80]}
c={'name':'柠檬班华华','age':'未知','class':'柠檬班VIP班级'}
a.update(c)
print(a)