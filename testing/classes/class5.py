# -*- coding: UTF-8 -*-


from classes.class4 import Dog,Dog1


# ChineseDog继承Dog类
class ChineseDog(Dog,Dog1):
    # 品种
    # 重写类变量
    dogtype = '中华田园犬'

    # 重载构造函数
    # 构造方法
    def __init__(self, n):
        super().__init__(n)
        self.name1 = n
        print('这是ChineseDog的构造方法：' + str(n))

    # # 重写父类方法
    # def eat(self):
    #     print(self.name + '在啃骨头')

    # 扩展
    def yaoweiba(self):
        print(self.n + "在摇尾巴")

