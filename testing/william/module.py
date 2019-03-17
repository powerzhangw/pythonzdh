# -*- coding: UTF-8 -*-
import requests
# 课程实用技能库
print('module模块被调用')

# 阶乘
def jiecheng(n):
    '''
    :param n:阶乘数
    :return: 空
    :作用：主要给大家讲递归的原理
    '''
    # 出口
    if n == 1:
        return 1
    else:
        # 当n大于1时，n! = n * (n-1)!
        return n * jiecheng(n - 1)


# 快排
def quickSort(list1, l, h):
    # 定义临时变量，保存原来的边界
    '''
    :param list1:需要排序数列
    :param l:左边界
    :param h:右边界
    :return:空
    :作用：主要给大家讲解快排的原理，不要笔试的时候写不出来
    '''
    ll = l
    hh = h

    # 定义最后一个为基准
    base = list1[h]

    # 反复执行寻找的操作，直到l=h
    while l < h:
        # 从左往右找，循环结束的条件是l=h
        while l < h:
            if list1[l] > base:
                list1[l], list1[h] = list1[h], list1[l]
                # 如果从左往右找到并交换了比base大的元素，我们把h左移一位
                h = h - 1
                break
            else:
                # 没找到就继续
                l = l + 1

        # 从右往左找，循环结束的条件是l=h
        while l < h:
            if list1[h] < base:
                list1[l], list1[h] = list1[h], list1[l]
                l = l + 1
                break
            else:
                h = h - 1

    #递归的左边出口
    if l == ll:
        return
    else:
        quickSort(list1,ll,l-1)

    # 递归的右边出口
    if h==hh:
        return
    else:
        quickSort(list1,h+1,hh)


# 选择排序
def selectSort(height):
    # 外层循环代表轮次
    l = len(height)
    for i in range(0, l):
        # 内层循环，选择最大的
        # 以第一个人为基准，记录下标
        tmp = 0
        for j in range(1, l - i):
            if height[tmp] < height[j]:
                # 记录最大值下标
                tmp = j

        # # 把最高的放到最后
        t = height[tmp]
        height[tmp] = height[l - i - 1]
        height[l - i - 1] = t


# 冒泡排序
def bubbleSort(height):
    for i in range(0, len(height) - 1):
        # 内层循环完成比较和交换
        for j in range(1, len(height) - i):
            if height[j - 1] > height[j]:
                height[j - 1], height[j] = height[j], height[j - 1]


# 输出杨辉三角
def getYH(yh):
    # l1用来存储上一行的系数
    l1 = [1]
    # l2用来存储下一行的系数
    l2 = [1, 1]

    # 控制杨辉的次方
    for i in range(0, yh + 1):
        # 直接输出当前行
        # 输出前面没有内容的一半yh的长度
        for ii in range(i, yh):
            print("%2s" % ' ', end='')

        for ii in range(len(l1)):
            print("%-4s" % l1[ii], end='')
        print()
        # 通过循环得到下一行
        for j in range(0, i + 2):
            # 判断是第一个或者最后一个，它的值就是1
            if j == 0 or j == i + 1:
                l2[j] = 1
            else:
                # 不是边界的时候
                l2[j] = l1[j - 1] + l1[j]

        # 复制l2的元素到l1，l2就变成了上一行
        l1 = l2[0:]
        # l2将要存储的下一行，多一个系数
        l2.append(1)
