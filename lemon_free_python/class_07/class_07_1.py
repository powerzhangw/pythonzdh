# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 22:39
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_07_1.py

#字典
#1：标志 {}  关键字 dict
#2:a={} 空字典
#3:字典的数据存储格式是 key:value  键值对
#4:字典里面value可以是任何类型的数据
#5：取值方式：根据key取值  字典名[key]
a={'name':'华华','age':18,'money':99.99,'score':[100,100,80]}
#1）新增一个元素 字典名[new_key]=value  new_key不存在当前字典里面
a['sex']='girl'

#2）修改一个元素的值 字典名[old_key]=value old_key存在当前字典里面
a['money']=1000

#3）删除操作
#a.clear() #清空
a.pop('score')
print(a)
