# -*- coding: UTF-8 -*-
import json

list1 = [1, 2, 3, 4, 2, 5, 6]
for index in range(len(list1)):
    print(list1[index])
    list1[index] = 1

print(list1)
s = '1;2;3;4;5;6;7'
s1 = s.split(';')
print(s1)

tup1 = (1, 2, 3)
tup2 = (4,)
tup3 = tup1+tup2
print(tup3)


tup = ('male', 'female', 'renyao')
print(tup)

for i in range(len(tup)):
    print(tup[i])

for item in tup:
    print(item)

dict1 = {
    'k1': 1,
    'k2': 2.0,
    'k3': "33",
    'k4': True
}

print(type(dict1['k2']))
print(len(dict1))
dict1['k3'] = 'william'
print(dict1)
# dict1.pop('k2')
# print(dict1)
del dict1['k2']
print(dict1)
# dict1.clear()
dict1['k2'] = 1.111
print(dict1)

dict2 = {
    'kk': 'tt'
}

dict1.update(dict2)
print(dict1)

# 默认获取key，和in dict1.keys()
for key in dict1:
    print(dict1[key])

for value in dict1.values():
    print(value)

# 获取一个键值对，返回一个元组
for item in dict1.items():
    print(item)
    print(item[0] + ':' + str(item[1]))

for key, value in dict1.items():
    print(key + ":" + str(value))


# #####################dict的应用######################

s = '{"status":"0","t":"1543844862168","set_cache_time":"","data":' \
    '[{"location":"澳大利亚","titlecont":"IP地址查询","origip":"1.1.1.1",' \
    '"origipquery":"1.1.1.1","showlamp":"1","showLikeShare":1,"shareImage"' \
    ':1,"ExtendedLocation":"","OriginQuery":"1.1.1.1","tplt":"ip",' \
    '"resourceid":"6006","fetchkey":"1.1.1.1","appinfo":"","role_id":0,' \
    '"disp_type":0}]}'

dictjson = json.loads(s)

print(dictjson['data'][0]['location'])

s2 = str(dictjson)
s2 = s2.replace("'",'"')
print(s2)