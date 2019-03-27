# -*- coding: utf-8 -*-
# @Author : "powerzhang"
import random
import string

def get_businessNumber():
    random_string = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    my_string = random_string.lower()
    return my_string
bus = get_businessNumber()
print(bus)

# 随机整数：
a = random.randint(1,50)
print(a)

# 随机选取0到100间的偶数：
b = random.randrange(0, 101, 2)
print(b)

# 随机浮点数：
c= random.random()
print (a)
# print random.uniform(1, 10)

# 随机字符：
bus = random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
print("bus{0}:",format(bus))
print(bus)

# 多个字符中生成指定数量的随机字符：
# print random.sample('zyxwvutsrqponmlkjihgfedcba',5)
#
# # 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
print (ran_str)
#
# # 多个字符中选取指定数量的字符组成新字符串：
# prin ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
#
# # 随机选取字符串：
# print random.choice(['剪刀', '石头', '布'])
#
# # 打乱排序
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print random.shuffle(items)