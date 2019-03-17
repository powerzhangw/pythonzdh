# -*- coding: UTF-8 -*-
from decimal import Decimal

print('############################下面是结果###########################')

# 将课程九九乘法表，以while循环实现
# 两个数相乘，都是从1-9递增
# 先控制x循环递增到9
print('# 将课程九九乘法表，以while循环实现')
x = 1
while x < 10:
    # 在循环里面，再控制y循环递增到9
    # 每一个x都会和9个y相乘
    # 定义每行显示的内容
    # ''代表长度为0的字符串，就是没有字符
    row = ''
    y = 0
    while y < 9:
        y += 1
        row += str(x * y) + '\t'

    print(row)
    x += 1

print()
# 四舍五入保留两位小数
print('# 四舍五入保留两位小数')
f = 100.0000
print(round(f, 3))
f = '%.3f' % f
print(f)
f = 100.5555
print(Decimal(f))
print(round(f, 3))
f = '%.3f' % f
print(f)
f = 100.5555
f = Decimal(str(f)).quantize(Decimal('0.000'))
print(f)

print()
# 用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？
print('用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？')
# 判断字符串长度的函数：len()
print('请在此输入用户名：')
loginname = input()
print('请输入您的密码：')
password = input()
# Python里面空指针是None，不是null
loginname = None
if loginname is None or password is None:
    print('用户名密码不能为空！')
else:
    if len(loginname) < 6 or len(password) < 6:
        print('用户名密码不能小于6位字符！')
    else:
        if len(loginname) > 16 or len(password) > 16:
            print('用户名密码不能大于16位字符！')
        else:
            print('用户名密码合法！')

print()
# 九九乘法表去掉对角线
print('# 九九乘法表去掉对角线')
x = 1
while x < 10:
    row = ''
    y = 0
    while y < 9:
        y += 1
        # 第一条对角线条件是x==y
        if x == y:
            row += ' ' + '\t'
            continue
        # 第一条对角线条件是x+y==10
        if x + y == 10:
            row += ' ' + '\t'
            continue

        row += str(x * y) + '\t'

    print(row)
    x += 1
