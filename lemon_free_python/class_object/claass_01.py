# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 15:00
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : claass_01.py

#类
#汽车类  单车类  动物类 人类  植物类
#他们具有共同的特征===划分为一个类
#标准：编写代码的人来定义这个

#男朋友类
#身高：175  money:20万  会做饭  喜欢户外运动 会游泳   会写代码
#姓名 年龄

#在Python 如何用代码表达出来？
#Python类与对象的知识
#关键字 class  类里面一般包含 属性以及函数
# class  类名：
# '''类的注释'''
# #     #属性
# #     #函数


#男朋友类
#身高：175  money:20万  会做饭  喜欢户外运动 会游泳   会写代码
#姓名 年龄

class BoyFriend:
    #属性
    height=175
    money=200000
    name="周杰伦"
    年龄=28

    #行为特征--->函数-->80%的相似度 跟普通函数
    def cooking(self):
        print("会做饭")

    def hiking(self):
        print("喜欢户外运动")

    def swimming(self):
        print("喜欢游泳")

    def coding(self):
        print("会写代码")

#怎么来调用类里面的属性和函数呢？  ----通过实例/对象
#创建实例： 类名()
#调用方法 实例.方法
#调用属性  实例.属性

bf=BoyFriend()
bf.coding()
bf.cooking()

print(bf.height)
print(bf.money)

print("***********")
bf_2=BoyFriend()
bf_2.cooking()
bf.swimming()