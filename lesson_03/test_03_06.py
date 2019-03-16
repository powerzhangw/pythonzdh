'''
a=3
while(a<5):
    print('test')
    if(a==3):
        break
'''

import time
from lesson_03.com import driver
from lesson_03.search_page import  train_No,train_num


driver.get('http://trains.ctrip.com/TrainBooking/Search.aspx?from=shanghai&to=hangzhou&day=2019-01-03&number=&fromCn=%25E4%25B8%258A%25E6%25B5%25B7&toCn=%25E6%259D%25AD%25E5%25B7%259E')
driver.maximize_window()
train_No(9)
train_num("K1805")