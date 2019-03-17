# -*- coding: UTF-8 -*-

print('============作业1：面向过程的编程示例============')
# 定义字符串变量，存放事件过程
proc = 'Will早上起床；' + '然后穿好衣服，刷牙，洗脸；' \
       + '小帅哥高高兴兴去上学啦！'
print(proc)

print()
print('=============作业2：解方程，求z的值==============')
# 设x=3,y=4
x = 3
y = 4
z = x ** 2 + y ** 3
print('z=x^2+y^3=' + str(z))

print()
print('==========作业3：课外作业，业务逻辑分析===========')
# 业务最开始，老婆的需求
print("下午，老婆打电话对你说：“老公，晚上回来买一个西瓜，如果看到西红柿，就买两个。”")
print("挂电话，继续工作...")
print("6点了，终于下班了，关电脑，走人...")
print("路过菜市场，老婆好像要买西瓜。")
print("先买了一个西瓜。")
# 请输入看到到西红柿？0：没有；1：有
print('请输入看到到西红柿？0：没有；1：有')
# 从控制台接收用户输入
tomato = input()
if tomato == '1':
    print("沉思，我应该买两个西瓜还是买两个西红柿？")
    print("问需求方，打电话：\"老婆，我看到西红柿了，是买两个西瓜还是买两个西红柿？\"")
    # 需求方回复0：西瓜；1：西红柿
    print('需求方回复0：西瓜；1：西红柿')
    choose = input()
    if choose == '0':
        print("回头买西瓜，走回家")
    else:
        print("买俩西红柿，走回家")
else:
    print("拎着一个西瓜，走回家")