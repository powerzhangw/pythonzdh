# -*- coding: utf-8 -*-
# @Author  : powerzhang    now=time.strftime("%Y-%m-%d %H_%M_%S")
import os
import time
import random



import random

li = []
for i in range(32):
    """
    随机生成32位大写字母和数字的验证码
    """
    r = random.randrange(0, 32)
    if r == 4 or r == 2:  # 如果随机数为2或4就生成数字
        temp = random.randrange(0, 10)  # 生成随机数字
        li.append(str(temp))  # int型无法用list的join方法，用str转换为字符串
    else:  # 否则随机生成字母
        temp = random.randrange(65, 91)  # 数字对应的ascii码数字对应的字符
        c = chr(temp)
        li.append(c)

result = "".join(li)  # join把列表所有元素拼接为一个字符串时，要求所有元素都是字符串
print(result)

def random_num():
    code = ''
    for i in range(32):
        ran1 = random.randint(0,9)
        ran2 = chr(random.randint(65,90))
        add = random.choice([ran1,ran2])
        code = ''.join([code,str(add)])
    return code

rand_n = random_num()
print(rand_n)

def generate_code(self):
    # 定义一个种子，从这里面随机拿出一个值，可以是字母
    seeds = "1234567890"
    # 定义一个空列表，每次循环，将拿到的值，加入列表
    random_num = []
    # choice函数：每次从seeds拿一个值，加入列表
    for i in range(4):
        random_str.append(choice(seeds))
    # 将列表里的值，变成四位字符串
    return "" . join(random_str)



# now=time.strftime("%Y%m%d%H")
# print(now)
#
# # 当前路径
# a = os.getcwd()
# print(a)
# case_path = os.path.join(os.getcwd(), "test_case")
# print(case_path)

