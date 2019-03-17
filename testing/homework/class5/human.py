# -*- coding: UTF-8 -*-


# 人类
class Human:
    # 类变量：我是一个人
    myself = '我是一个人'

    # 构造函数
    def __init__(self,n):
        # 实例变量
        self.name = n

    # 定义说话的函数
    def say(self):
        print('hello, I\'m ' + self.name)

    # 定义运动方法
    def play(self):
        print('生命源于运动')

    # 定义类方法，访问类属性
    @classmethod
    def self(cls):
        print(cls.myself)
