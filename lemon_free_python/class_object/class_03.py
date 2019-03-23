# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 17:21
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_03.py
class BoyFriend:
    #属性
    def __init__(self,height,money,name,age):
        self.height=height
        self.money=money
        self.name=name
        self.age=age

    #行为特征--->函数-->80%的相似度 跟普通函数  20% 不相似的地方?  self
    @classmethod
    def cooking(cls):#类里面的函数与普通函数的区别
        print("会做饭")

    @staticmethod
    def hiking():
        print("喜欢户外运动")

    #类里面的函数---实例方法/实例
    def swimming(self,long):
        print(self.name+"喜欢游泳,一次可以游{0}米".format(long))

    def coding(self,long,*args):
        self.swimming(long)#参数化
        return (self.name+"会写{0}代码".format(args))

bf=BoyFriend(180,2000000,'nick',22)
res=bf.coding(100,"java","Python","shell")
print("return之后的结果",res)
#实例方法：
#如果是调用类里面的属性 self.属性名
#如果是实例方法自己带参数  参数传递的规则 同普通函数

#下节课 类方法之间的调用 return

#初始化函数