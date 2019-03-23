# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 19:39
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_while_break_continue.py
#主题：结合break以及continue防止这个while循环进入死循环
#while:   break...continue...
#break:结束循环
#continue：结束本次循环继续下一次循环

a=10
while True:#死循环的必要条件
    a-=1#每次对a减去1 a=a-1
    if a>0:
         print("a的值：{0}".format(a))
         continue
    else:
        break

#while 跟if的结合使用  continue以及break