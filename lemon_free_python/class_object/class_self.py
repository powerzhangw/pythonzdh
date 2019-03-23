# -*- coding: utf-8 -*-
#类包含 属性和函数
class BoyFriend:
    #属性
    height=175
    money=200000
    name="周杰伦"
    年龄=28

    #行为特征--->函数-->80%的相似度 跟普通函数  20% 不相似的地方?  self
    def cooking(self):#类里面的函数与普通函数的区别
        # print("打印self",self)#self为何物
        print("会做饭")

    def hiking(self):
        print("喜欢户外运动")

    def swimming(self):
        print("喜欢游泳")

    def coding(self):
        print("会写代码")

#直接以实例调用
bf=BoyFriend()
print("打印bf实例",bf)#打印实例 内存地址
bf.cooking()

#把实例作为参数传递进去
bf_1=BoyFriend
bf_1.cooking(BoyFriend())