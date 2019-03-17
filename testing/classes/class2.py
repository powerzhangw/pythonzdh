# -*- coding: UTF-8 -*-


# x = 1
# y = 3
#
# # x/y的余数
# z = x % y
# print(z)
# # 取整
# z = int(x / y)
# print(z)
# # 不四舍五入保留两位小数
# z = int(x / y * 100) / 100
# print(z)
#
# # 字符串的比较
# str1 = 'aa'
# str2 = 'bbaa'
# # 相等
# print(str1 == str2)
# # 包含
# print(str2.__contains__(str1))
#
# # 逻辑运算
# bool1 = False
# bool2 = False
# # and
# print(not True)
#
# # 当x>1 且 y<2时，(当w>1 z=x+y；否则 z = x + w)否则z=x-y
# # True and False
# if x > 1 > 0 and y < 2:
#     z = x + y
# else:
#     z = x - y
# print(z)
#
# x = 1
# x = x > 1
# print(x)
#
# x = 2
# print(not x > 3)
#
# # 求|x|
# x = -1
# if x >= 0:
#     z = x
# else:
#     z = -x
# print(z)
#
# # 求：z = |x| + |y|
# x = -1
# y = 2
# if y >= 0:
#     if x >= 0:
#         z = x + y
#     else:
#         z = -x + y
# else:
#     if x >= 0:
#         z = x - y
#     else:
#         z = -x - y
# print(z)
#
# # while循环
# d = 1
# # 七天之内
# while d < 8:
#     # d += 1
#     # 周一到周五上班
#     if d < 6:
#         print("星期" + str(d) + "：上班")
#     else:
#         print("星期" + str(d) + "：玩去咯")
#     d += 1
#
# # 字符串的in
# s = "hello will"
# for ss in s:
#     print(ss)
#
# z = 0
# for i in range(1, 101):
#     z += i
#
# print(z)

x = 0
y = 0
i = x + y
xx = 0
yy = 0
while i < 13:
    x += 1
    y += 1
    i = x + y
    xx += x
    yy += y

# print(xx)
# print(yy)

# 九九乘法表
z = 0
s = ''
for i in range(1, 10):
    s = ''
    for j in range(1, 10):
        if i == j:
            s += ' ' + "\t"
            continue
        z = i * j
        s += str(z) + "\t"

    print(s)

s = ''
print(s.__len__())
