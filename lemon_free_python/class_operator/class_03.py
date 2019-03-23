# -*- coding: utf-8 -*-
# @Time    : 2018/10/7 11:05
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_03.py
#比较运算符
#> >= < <= != ==
#返回的值类型是：布尔值  True False
# a=1
# b=3
# print(a!=b)

#逻辑运算符  and or  not  返回的值类型是：布尔值  True False
# age=18
# sex='girl'
# print(age>20 or sex!='girl')
#and 左右两边都成立 才为真  返回True
#or 左右两边只要有一边为真  就会返回True 否则 两边都不成立 就会返回False

#真真为真   假假为假

#成员运算符 in not in 返回的值类型是：布尔值  True False
# #判断某个元素是否存在于我们的数据里面
# # s='lemon'
# # L=[1,2,3,4,'HELLO']
# # c={'name':'柠檬班华华','age':'未知','class':'柠檬班VIP班级'}
# # print('柠檬班华华' in c.values())#key来定位元素
#
# # 需求：给定一个只包含正整数且非空的列表，返回该列表中重复次数最多的前N个数字
# # （返回结果按重复次数从多到少降序排列，N不存在取值非法的情况），
# # 请用python语言实现该需求  。。。。。10分钟内写出来
a=[1,6,7,4,4,5,4,5,4,5,5,6,7,8,5,6,7,3,4,2,2,1,4,8,9,4,5,6]
c={}#空字典
for item in set(a):#利用set对a去重，且作为c字典的key
    c[item]=a.count(item)#利用列表的count方法 统计key的数目作为key的value存储到c字典
print(c)
# d=[]#空列表
# res=sorted(c.values(),reverse=True)#对数据进行倒序排序(多的在前面，少的在后面），并存储到res
# for num in res:#遍历value值（在上面已经根据出现次数的大小进行了排序)
#     for key,value in c.items():#遍历键值对
#         if num==value and key not in d:#把数字按照出现的次数来进行排序
#             d.append(key)
# print(d)

# e={1, 2, 3, 4, 5, 6, 7, 8, 9}
# f={1,66,88}
# #并集
# print(e|f)
# print(e.union(f))
#
# #差集
# print(e-f)
# print(e.difference(f))
#
# #交集
# # print(e.intersection(f))
# # print(e&f)

# L=[('b',2),('a',1),('c',3),('d',4)]
# print(sorted(L,key=lambda x:x[1],reverse=True))


# a=[1,6,7,4,4,5,4,5,4,5,5,6,7,8,5,6,7,3,4,2,2,1,4,8,9,4,5,6]
# b=['hello','lemon']
# print(a.count(4))
# # a.extend(b)
# # print(a.index(4))
# # a.reverse()
# # print(a)
# a.remove(4)
# # a.sort()
# print(a)
# a="1234567"
# b=list(a)
# b.reverse()
# c="".join(b)
# print(c)

# a={'name':'华华','age':18,'money':99.99,'score':[100,100,80]}
# a={"name":"柠檬班华华","age":"20"}
# b={"sex":"girl","money":1000}
# # b=a.get('name')
# # b=a.items()
# # b=a.keys()
# # a.popitem()
# # b=a.setdefault("name","柠檬班华华")
# c=a.update(b)
# # b=a.values()
# print(a)

# keys = ["A","B","C"]
# values = ["1","2","3"]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)
# print(dict(zip(keys,values)))