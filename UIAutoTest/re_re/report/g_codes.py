# -*- coding: utf-8 -*-
# @Author : "powerzhang"

# "fileNumber": get_cod,
import time

def get_codes():
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    my_code = str(now_time)[0:13]
    f = open('C:\\txt.txt','w')
    f.write(my_code)
    f.close()
    return my_code

"fileNumber": get_cod