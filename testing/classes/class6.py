# -*- coding: UTF-8 -*-

import time, sys, threading
from william import *

n = module.jiecheng(4)
print(n)

l = [1, 3, 5, 7, 2, 4, 8, 10, 0]
module.quickSort(l,0,len(l)-1)
print('快排')
print(l)

l = [1, 3, 5, 7, 2, 4, 8, 10, 0]
module.selectSort(l)
print('选择')
print(l)

l = [1, 3, 5, 7, 2, 4, 8, 10, 0]
print('冒泡')
module.bubbleSort(l)
print(l)

print('杨辉三角')
module.getYH(11)


# 局部变量和全局变量
# 全局变量：在整个脚本里面生效的
# g = 1
#
# def testg():
#     # 告诉函数，g是全局变量
#     global g
#     g = 2
#     # gg局部变量：只在当前函数生效
#     gg = 1
#     print(g+gg)
#
# def testf(ggg):
#     # 告诉函数，g是全局变量
#     global g
#     print(g)
#
#
# testg()
# testf(1)

# 函数的定义
# 定义一个把字符串转换为整数的函数
# def test(list2):
#     # 传地址的话，不要直接对list2进行赋值
#     # 可以改变list2里面的钥匙
#     list2[0] = 0
#
#
# list1 = [1, 2, 3, 4]
# test(list1)
# print(list1)

# a = 3
# b = [1,'2']
# c = '2'
# print(id(a))
# print(id(b[1]))
# print(id(c))

# l1 = [3,2]
# l2 = [2,3,4]
# y =3
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# print(id(l2[2]))
# print(id(y))


# sys.setrecursionlimit(1000000)
# threading.stack_size(200000000)
# 
# 快速排序
def quickSort1(list1):
    # 停止递归的条件，当list1里面的元素少于2个
    if len(list1) < 2:
        return list1
    else:
        # 选取第一个为基准
        base = list1[0]
        # 遍历
        less = []
        equal = []
        greater = []
        for item in list1:
            if item < base:
                # 将所有小于基准的元素放到左边的数列
                less.append(item)
            else:
                if item == base:
                    # 将所有等于于基准的元素放到中间的数列
                    equal.append(item)
                else:
                    # 将所有大于基准的元素放到右边的数列
                    greater.append(item)

        return quickSort1(less) + equal + quickSort1(greater)

# 
# # 快速排序
# def quickSort(list1, l, h):
#     # 停止递归的条件，当list1里面的元素少于2个
#     if l == h:
#         pass
#     else:
#         # 保存排序前的边界
#         low = l
#         high = h
#         # 选取最后一个为基准
#         base = list1[h]
#         # 当l<r，也就是还没有比较完
#         while l < h:
#             # 从左往右，找比base小的，交换到h位置
#             while l < h:
#                 if list1[l] < base:
#                     list1[l], list1[h] = list1[h], list1[l]
#                     # 右边标记左移
#                     h = h - 1
#                     break
#                 else:
#                     # 一直往右找
#                     l = l + 1
# 
#             # 从右往左，找比base大的，交换到l位置
#             while l < h:
#                 if list1[h] > base:
#                     list1[l], list1[h] = list1[h], list1[l]
#                     # 左标记右移
#                     l = l + 1
#                     break
#                 else:
#                     # 一直往左找
#                     h = h - 1
# 
# 
#         if low < l:
#             quickSort(list1,low,l-1)
# 
#         if high > h:
#             quickSort(list1,h+1,high)
# 
# 
# # height = [190, 187, 172, 160, 163, 166, 173, 182, 165, 159]
# # quickSort(height, 0, len(height)-1)
# # print(height)
# 
# def testSort():
#     h = []
#     for i in range(20000):
#         h.append(i)
# 
#     height = h[0:]
#     l = len(height)
#     t1 = int(time.time())
#     print('开始快速排序')
# 
#     quickSort(height,0,len(height)-1)
# 
#     t2 = int(time.time())
#     print('快速排序耗时:' + str(t2 - t1))
# 
# 
# thread = threading.Thread(target=testSort)
# thread.start()
