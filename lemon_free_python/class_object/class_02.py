# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 16:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_02.py
#类里面的函数
#1：类函数/类方法  @classmethod 可以通过类名直接调用
#什么时候去定义为类方法的？  1：如果你想直接通过类名.函数名调用  2：类方法跟类属性没有直接的关联
#3：当我们有初始化函数的时候 可以直接定义为类方法

#  2：实例函数/方法---常用的

# 3：静态函数/静态方法 @staticmethod#
# 1：如果你想直接通过类名.函数名调用  2：类方法跟类属性没有直接的关联  不能直接调用属性
#3：当我们有初始化函数的时候 可以直接定义为类方法
class BoyFriend:
    #属性
    height=175
    money=200000
    name="周杰伦"
    age=28

    #行为特征--->函数-->80%的相似度 跟普通函数  20% 不相似的地方?  self
    @classmethod
    def cooking(cls):#类里面的函数与普通函数的区别
        print("会做饭")

    @staticmethod
    def hiking():
        print("喜欢户外运动")

    #类里面的函数---实例方法/实例
    def swimming(self):
        print("喜欢游泳")

    def coding(self):
        print("会写代码")

#直接以实例调用
# bf=BoyFriend()
# bf.cooking()
# bf.hiking()
#
# BoyFriend.cooking()
# BoyFriend.hiking()

BoyFriend().swimming()
BoyFriend.swimming(BoyFriend())

#类方法 实例方法 静态方法
#1：都可以被实例调用
#2：只有静态方法以及类方法 可以直接通过类名.函数名()
#3: 静态方法和类方法 不能调用类属性