# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 20:10
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_06_2.py
#列表支持增加删除修改
# a=[1,0.05,'lemonban',(1,2,3),[4,5,6]]
#1：新增操作：
#1）列表名.append() 加元素到列表的最后面  每次只能添加一个元素
# a.append('柠檬班')
# a.append('华华')
# print(a)
#2）列表名.insert()  加元素到列表的指定位置
# a.insert(0,'华华')
# print(a)

#2：修改列表的元素值  重新赋值 =赋值运算符
# a[-1]='热爱学习的我'
# print(a)

#3：删除元素
#1）列表名.pop() 删除列表的最后面一个元素
a=[1,0.05,'lemonban',(1,2,3),[4,5,6]]
# a.pop()
# print(a)

#1）列表名.pop(index) 删除列表指定尾椎的元素
# a.pop(2)
# print(a)

#4:其他操作
c=[7,12,5,60,3,22,56]
#c.sort() 排序
# c.reverse() 倒置
# c.clear()
print(c)