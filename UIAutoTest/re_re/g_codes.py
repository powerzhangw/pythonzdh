# -*- coding: utf-8 -*-import randomimport stringimport lib.logUntillog = lib.logUntil.Logimport timeimport requestsimport jsonname = "aaaa"def get_codes():    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))    my_code = str(now_time)[0:13]    f = open('C:\\txt.txt','w')    write = f.write(my_code)    f.close()    return my_codea = get_codes()print(a)def get_code():    f = open('C:\\txt.txt','r')    code = f.read()    f.close()    return codedef randomname():    xing='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'    ming='豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'    X=random.choice(xing)    M="".join(random.choice(ming) for i in range(2))    return (X+M)randomname()def times():    t1 = int(time.time())    t2 = str(t1) + '000'    time1 = int(t2)    return (time1)print("这是时间:",times())code = get_codes()codes = get_codes()print(code)print(codes)print("print(codes)")