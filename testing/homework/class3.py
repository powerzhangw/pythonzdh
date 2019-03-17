# -*- coding: UTF-8 -*-
import requests,json

print('############################下面是结果###########################')
# 列表，元组用while遍历实现
print("#1 列表，元组用while遍历实现")
# 列表while遍历
list1 = [1, 2, 3, 4, 5, 6, 7]
index = 0
while index < len(list1):
    print(list1[index], end=',')
    index += 1

# 元组while遍历
print()
tup1 = (1, 2, 3, 4, 5, 6, 8)
index = 0
while index < len(tup1):
    print(tup1[index], end=',')
    index += 1

# 字典四种遍历实现
print("#2 字典四种遍历实现")
print()
dict1 = {
    'k1': 1,
    'k2': 2.0,
    'k3': "33",
    'k4': True
}
# 默认获取key，和in dict1.keys()
print("###########key遍历###########")
for key in dict1:
    print(key, end=", ")

print("\n###########value遍历###########")
for value in dict1.values():
    print(value, end=", ")

# 获取一个键值对，返回一个元组
print("\n###########元素遍历###########")
for item in dict1.items():
    print(item[0] + ':' + str(item[1]), end=", ")

print("\n###########key：value遍历###########")
for key, value in dict1.items():
    print(key + ":" + str(value), end=", ")

print("\n\n#3 自己去抓包，把ip接口的返回结果处理为标准json字符串；再使用json库，把字符串转为dict，并打印你所在地区的location")
result = requests.get('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php','query=175.10.38.136&co=&resource_id=6006&t=1543891259207&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110201736145552476669_1543891237139&_=1543891237144')
result = result.text
result = result[result.find('{'):result.rfind('}')+1]
result = json.loads(result)
print(result['data'][0]['location'])

