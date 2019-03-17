# -*- coding: UTF-8 -*-

import time

# 构造了一万个要排序的数据，他们是升序的
h = []
for i in range(10000):
    h.append(i)

height = h[0:]
l = len(height)
t1 = int(time.time())
print('开始选择排序')
# 外层循环代表轮次
for i in range(0, l - 1):
    # 内层循环，选择最大的
    # 以第一个人为基准，记录下标
    tmp = 0
    for j in range(1, l - i):
        if height[tmp] < height[j]:
            # 记录最大值下标
            tmp = j

        # # 把最高的放到最后
    height[tmp], height[j] = height[j], height[tmp]
t2 = int(time.time())
print('选择排序耗时:' + str(t2 - t1))

# height = h[0:]
# l = len(height)
# t1 = int(time.time())
# print('开始系统的排序')
# # 外层循环代表轮次
# height.sort()
# t2 = int(time.time())
# print('选择排序耗时:' + str(t2 - t1))
#
#
# height = h[0:]
# l = len(height)
# t1 = int(time.time())
# print('开始冒泡排序')
# # 外层循环代表轮次
# for i in range(0, l - 1):
#     # 内层循环完成比较和交换
#     for j in range(1, l - i):
#         if height[j - 1] < height[j]:
#             height[j - 1], height[j] = height[j], height[j - 1]
#
# t2 = int(time.time())
# print('耗时:' + str(t2 - t1))
#
# height = h[0:]
# l = len(height)
# t1 = int(time.time())
# print('开始选择的排序')
# # 外层循环代表轮次
# for i in range(0, l - 1):
#     for j in range(i + 1, l):
#         if height[i] < height[j]:
#             height[i], height[j] = height[j], height[i]
#
# t2 = int(time.time())
# print('耗时:' + str(t2 - t1))
