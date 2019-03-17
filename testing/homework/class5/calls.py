# -*- coding: UTF-8 -*-
from homework.class5.male import Male
from homework.class5.female import FeMale


boy =Male('A')
print('# 体现方法的继承和实例变量的重写')
# 体现方法的继承和实例变量的重写
boy.say()
print('# 体现类方法和类属性的重写')
# 体现类方法和类属性的重写
Male.self()
print('# 体现扩展')
# 体现扩展
boy.love('B')
print('# 体现实例方法的继承')
# 体现实例方法的继承
boy.play()


girl =FeMale('B')
print('# 体现方法的继承和实例变量的继承')
# 体现方法的继承和实例变量的继承
girl.say()
print('# 体现类方法和类属性的继承')
# 体现类方法和类属性的继承
FeMale.self()
print('# 体现扩展')
# 体现扩展
girl.love('A')
print('# 体现实例方法的继承')
# 体现实例方法的继承
girl.play()
