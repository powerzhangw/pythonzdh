# -*- coding: UTF-8 -*-
from homework.class5.human import Human


# 女人类
class FeMale(Human):

    # 构造函数
    def __init__(self,n):
        Human.__init__(self,n)
        # 定义自己的男朋友
        self.boyf = None

    # 定义谈恋爱的函数，方法扩展
    def love(self,g):
        if self.boyf is None:
            print('开始和' + g + '谈恋爱！')
            self.boyf = g
        else:
            print('换一个帅哥：' + g + '，谈恋爱！')
            self.boyf = g

    # 定义运动方法，重写运动
    def play(self):
        print('运动才能保持身材')
