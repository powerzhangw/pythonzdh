# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 13:48
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_for_for.py
#嵌套for循环  for循环里面还有一个循环
# list_1 = [
#     [2, 3, 8, 4, 9, 5,9,11],
#     [5, 6, 10, 17, 11, 2]
# ]
# #请把列表以及字列表里面的每一个元素挨个打印出来
# for item in list_1:
#     for value in item:
#         print("数据：",value)
        # print("数据类型：",type(value))
    # print(item[0])
    # print(item[1])
    # print(item[2])
    # print(item[3])
    # print(item[4])
    # print(item[5])


#利用嵌套for循环打印一个直角三角形到控制台  三角形底边长度为5 元素都是*
#* 1
#** 2
#*** 3
#**** 4
#***** 5
# for i in range(1,6):#1 2 3 4 5
#     # print("现在是第{0}行".format(i))
#     for j in range(i):#i=1 j 0  i=2 j=0 1  i=3 j=0 1 2
#         print("*",end='')#控制不换行输出
#     print("")#这里是表示for循环结束后 换行

#99乘法表
#1*1=1
#1*2=2 2*2=4
#1*3=3 2*3=3 3*3=9
#1*4=4 2*4=8 3*4=12 4*4=16
#....
for i in range(1,10):#i=1 i=2
    # print("目前在第{}行".format(i))
    for j in range(1,i+1):#i=i j=1 i=2 j= 1 2  i=3 j=1 2 3
        print("{0}*{1} ={2} ".format(j,i,i*j),end="")#控制此for循环里面的内容不换行
    print("")#for循环结束后 换行

#安排一个题目：
#利用嵌套for循环 完成冒泡排序
#拓展：冒泡算法是什么？
L=[4,9,10,5,111,3,244]
#答案找谁？  找我们柠檬班的毛毛辅导员 742717718