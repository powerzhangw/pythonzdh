# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 16:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_02_1.py
#语法：必须要遵守的规范 方法使用
#标识符：凡是在Python 我们自己命名的 自己取名字 都是标识符
#项目名 包名 模块名
#变量名 函数名 类名
#1：字母 下划线 数字组成 命名的时候 不能以数字开头
#2：见名知意：不同的字母和数字之间用下划线隔开
#class_basic_1(推荐）  classbasic1（不推荐）
#3:项目名 包名 模块名 变量名 函数名 都是小写字母，不同的字母之间用下划线隔开
#4：类名 首字母大写驼峰命名 StudentInfo  HttpRequest
#5:不能以关键字作为标识符  int str float class def.....

#行和缩进  利用缩进来控制代码的级别 tab
'''a = 1
if a > 0:#父级
    print('hello lemon!!hello huahua!')#子级
elif a < 0:
    print('hello a<0')
    if a<-3:
        print('hello a>-3')'''

#注释：  # 表示单行注释  快捷键 ctrl+/ ''' '''成对的三个单引号括起来的内容就是多行注释
#注释：这是一个备注信息？ 代码将不会被执行

#多行语句  连接符 \
# print('hello\
#       python\
#       6666 ')

#Python的引号 单引号 双引号 三引号
#成对的单引号 成对的双引号 三引号 括起来的内容 都是字符串
# a='4'
# b="888"
# c='''67890'''
# #type() 可以帮你判断数据的类型
# print(type(b))

#什么时候用什么引号？  都没有关系 你想怎么用就怎么用
# str_1='hello,\'华华\''
# #我们如果要把双引号或者是单引号作为字符串输出的一部分
# # 单引号和双引号分开 不能同时存在两个一样的单引号或者是双引号
#
# #转义 把一些特殊字符变成普通字符 r R \
# print(R"这是第一行\n这是第二行")

#Python文件里面的输入和输出
print('hello')#输出内容到控制台
a=input("请输入你心目中最好的课程机构")
#从控制台获取一个数据  数据类型是字符串
print(type(a))