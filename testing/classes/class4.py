# -*- coding: UTF-8 -*-


# 定义一个哈士奇狗类
class Dog:
    # 类变量
    # 品种
    dogtype = '哈士奇'
    # 二奶狗
    __seconddog = '藏獒'

    # 构造方法
    def __init__(self, n):
        self.name = n
        print('这是Dog的构造方法：' + str(n))

    # 叫
    def __bark(self, s):
        print(self.name + s)

    # 啃骨头
    def eat(self):
        print('狗在啃骨头')
        self.__bark('s')

    # 类函数
    # 类函数必须是用类来调用
    @classmethod
    def itstype(cls):
        print(cls.__seconddog)
        print(cls.dogtype)

    # 重载基础方法
    def __str__(self, s):
        print('我们重载了基础函数' + s)# 定义一个哈士奇狗类


class Dog:
    # 类变量
    # 品种
    dogtype = '哈士奇'
    # 二奶狗
    __seconddog = '藏獒'

    # 构造方法
    def __init__(self, n):
        self.name = n
        print('这是Dog的构造方法：' + str(n))

    # 叫
    def __bark(self, s):
        print(self.name + s)

    # 啃骨头
    def eat(self):
        print('狗在啃骨头')
        self.__bark('s')

    # 类函数
    # 类函数必须是用类来调用
    @classmethod
    def itstype(cls):
        print(cls.__seconddog)
        print(cls.dogtype)

    # 重载基础方法
    def __str__(self, s):
        print('我们重载了基础函数' + s)


# 定义一个哈士奇狗类
class Dog1:
    # 类变量
    # 品种
    dogtype = '哈士奇'
    # 二奶狗
    __seconddog = '藏獒'

    # 构造方法
    def __init__(self, n):
        self.name = n
        print('这是Dog的构造方法：' + str(n))

    # 叫
    def __bark(self, s):
        print(self.name + s)

    # 啃骨头
    def eat(self):
        print('狗在啃骨头')
        self.__bark('s')

    # 类函数
    # 类函数必须是用类来调用
    @classmethod
    def itstype(cls):
        print(cls.__seconddog)
        print(cls.dogtype)

    # 重载基础方法
    def __str__(self, s):
        print('我们重载了基础函数' + s)

# s = 'ab {{{bbb{ cca }bd}}} ab'
# # 切割
# ss = s.split(' ')
# print(ss)
# # 拼接
# sss = ' '.join(ss)
# print(sss)
#
# # 替换，默认替换全部
# t = s.replace('ab', 'cd')
# print(t)
# t = s.replace('ab', 'cd', -1)
# print(t)
#
# # 替换最后一个
# # 先反转，在替换反转后，最后反转回来
# ss = s[::-1]
# t = ss.replace('ba', 'dc', 1)
# t = t[::-1]
# print(t)
#
# # 先查找后截取
# # 从左往右找第一个
# l = s.find('{{{')
# print(l)
# # 从右往左找第一个
# r = s.rfind('}}}')
# print(r)
# # 截取
# t = s[l + 3:r]
# print(t)
l = [155, 187, 172, 160, 163, 166, 173, 182, 165, 159]

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

    # 交换
    # height[tmp], height[len(height) - i - 1] = height[len(height) - i - 1], height[tmp]

selectSort(l)
print(l)
# 
# # 冒泡排序
# height = [190, 187, 172, 160, 163, 166, 173, 182, 165, 159]
# # 外层循环代表轮次
# for i in range(0, len(height) - 1):
#     # 内层循环完成比较和交换
#     for j in range(1, len(height) - i):
#         if height[j - 1] > height[j]:
#             height[j - 1], height[j] = height[j], height[j - 1]
# 
# print(height)
# 
# # 杨辉三角
# # l1用来存储上一行的系数
# l1 = [1]
# # l2用来存储下一行的系数
# l2 = [1, 1]
# # yh用来存储杨辉三角的次数
# yh = 11
# yh = int(input("请输入杨辉的次方:"))
# 
# # 控制杨辉的次方
# for i in range(0, yh + 1):
#     # 直接输出当前行
#     # 输出前面没有内容的一半yh的长度
#     for ii in range(i, yh):
#         print("%2s" % ' ', end='')
# 
#     for ii in range(len(l1)):
#         print("%-4s" % l1[ii], end='')
#     print()
#     # 通过循环得到下一行
#     for j in range(0, i + 2):
#         # 判断是第一个或者最后一个，它的值就是1
#         if j == 0 or j == i + 1:
#             l2[j] = 1
#         else:
#             # 不是边界的时候
#             l2[j] = l1[j - 1] + l1[j]
# 
#     # 复制l2的元素到l1，l2就变成了上一行
#     l1 = l2[0:]
#     # l2将要存储的下一行，多一个系数
#     l2.append(1)
# 
# # # 杨辉三角
# # l1 = [1]
# # l2 = l1[0:]
# # l2.append(1)
# # try:
# #     yh = int(input("请输入杨辉次方数：\n"))
# #     yh = yh + 1
# # except:
# #     yh = 1
# #
# # for i in range(yh):
# #     for ii in range(i,yh-1):
# #         print("%3s" % ' ', end='')
# #     for yhs in l1:
# #         print("%-6s" % yhs, end='')
# #     print()
# #     for j in range(i + 2):
# #         if j == 0 or j == i + 1:
# #             l2[j] = 1
# #         else:
# #             l2[j] = l1[j - 1] + l1[j]
# #     l1 = l2[0:]
# #     l2.append(1)


