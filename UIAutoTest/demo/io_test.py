# -*- coding: utf-8 -*-
import os
# 生成一个文件夹
# os.mkdir('hellopower')
# 删除一个文件夹
# os.rmdir('hellopower')
# 当前目录 = os.getcwd()
# print(当前目录)
#获取当前目录并且包括当前文件
# path = os.path.realpath(__file__)
# 当前工程test_case_case路径
os.path.join(os.getcwd(), "test_case")
# print(path)
# 获取当前文件名
# pathname = os.path.basename(__file__)
# print(pathname)
# 函数拼接,在当前工作目录的test文件夹下创建sub_003
# new_path = os.path.join('test','sub_003')
# os.mkdir(new_path)
