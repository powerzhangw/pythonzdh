# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 14:50
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_04_5.py

str_1='@@@lem@@@on@@'
#5：字符串头尾的处理 strip()
res=str_1.strip('@')
print('处理后的结果：{}'.format(res))

#4：字符串的切割 split()
# res=str_1.split('o')#返回列表类型的数据  但是元素类型还是字符串
# print('切割后的结果：{}'.format(res))

#3：字符串的替换 replace（）函数  内建  可以指定替换次数
# res=str_1.replace('o','华华',1)#你要替换的目标字符  你要换上去的新值
# print('替换后的结果：{}'.format(res))

#2：字符串的查找 find()函数
# res=str_1.find('666')
# print('查找的结果：{}'.format(res))
#单个字符  如果能够找到 就返回单个字符在字符串里面的索引值
#子字符串  如果能够找到 就返回子字符串的第一个元素在原来字符串里面的索引值
#没找到  返回-1

#1:字符串的大小写切换 upper() lower()
# str_2='PYthON'
# res=str_2.lower()
# print('转换后的结果：{}'.format(res))

