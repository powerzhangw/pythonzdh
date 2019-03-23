# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 10:41
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_return.py
#函数式   面向过程return
#return 后面是0个参数  返回的就是None
#return 后面是1个参数  返回的就是你指定的参数 参数是什么类型 返回的就是什么类型
#return 后面有多个参数 >1 返回的参数 会放在一个元组里面

# def add():#隐式的添加一个return 但是return后面没有任何表达式 所以返回的就是None
#     print(5+6)
#     # return
#
# def add_2():
#     return 'hello',6
#
# print("第一个函数****")
# result_1=add()
# print("add函数运行的结果是：",result_1)
#
# print("第二个函数****")
# result_2=add_2()
# print("add_2函数运行的结果是：",result_2)
#return的作用：当你调用这个函数的时候 会返回一个结果
#这个结果值 你可以拿到之后 做进一步的处理
#2:如果没有return的话 那么返回的就是None

#什么时候用return：如果你想拿到某个函数的运行结果 那么就用return

#利用for循环  range函数 编写任意整数序列的求和函数
def add():
    count=0
    for i in range(1,101,1):
        count+=i
    print("函数内部打印求和结果是：",count)
    return count,666#多加了一个参数


result=add()
print("最终的函数运行结果是:",result)
#注意点：return 相当于一个结束信号  当函数遇到return 后面的代码将不会再执行
#return后面的代码不再执行！！

#两个助教：
