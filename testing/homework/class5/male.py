# -*- coding: UTF-8 -*-
from homework.class5.human import Human


# 男人类
class Male(Human):
    # 类变量：我是帅哥，重写类变量
    myself = '我是帅哥'

    # 构造函数
    def __init__(self,n):
        Human.__init__(self,n)
        # 实例变量名字，重写实例变量
        self.name = n
        # 定义自己的女朋友
        self.girlf = None

    # 定义谈恋爱的函数，方法扩展
    def love(self,g):
        if self.girlf is None:
            print('开始和' + g + '谈恋爱！')
            self.girlf = g
        else:
            print('换一个美女：' + g + '，谈恋爱！')
            self.girlf = g

    # 定义运动方法，重写运动
    def play(self):
        print('运动是我帅的根本')

    # 定义类方法，访问类属性，重写类方法
    @classmethod
    def self(cls):
        print(cls.myself)
