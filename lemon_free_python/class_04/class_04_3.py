# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 17:51
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_04_3.py
#1.格式化输出
age=18#存的是年龄  int
name='柠檬班华华'#存的是姓名 str
score=99.99
# #print(name+"，今年",age,'岁')
# #格式化输出 %d整数 %f浮点数 %s字符串
# print("%s今年%s岁,数学考了%s"%(name,age,score))#按顺序取值、
# #%d 必须放一个整数  %f可以放一个整数 也可以放一个浮点数 %s 可以放任意值

#第二种格式化输出 format {}
print("{0}今年数学考了{1}".format(name,score))#按顺序取值
#{}里面不指定数值 就会按顺序取值
#{}里面指定数值 就会根据你设置的去取值
#format里面的数据 也是有索引的 从0开始标记数据