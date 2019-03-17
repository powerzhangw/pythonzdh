# -*- coding: UTF-8 -*-

from testing.william import module

module.func1()

# 完成4个数字相加，求和
def sum(x, y, xx, yy):
    return x + y + xx + yy


z = 3
# 这是一个注释
'''这
    是
    一
    个
    注
    释'''
if z > 3:
    pass
else:
    print('否')

# 整数
x = 1.9
y = "1111.1"
yy = int(x)
print(x + yy)

# 字符串
string = 'taaa"\\\\bbb\''
print(string + str(x))

print(2 + False)

name = 'Will'
print(name + '起床啦')
print(name + '穿衣服')
print(name + '刷牙')
print(name + '洗脸')
print(name + '上学')

x = 2
y = x * 3 + 1
z = y * 10
print(z)
