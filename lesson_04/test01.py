import os
'''
print(os.getcwd()+'\\txt')
print(os.getcwd()[:-10])
print(os.getcwd()[0:3])
'''
#f = open('1.txt','r')
#print(f.read())
#print(f.read(1))
#print(f.readline())
#print(f.readlines())
#f = open('ww.txt','w')
#f.write("python selenium")
#f = open('w.txt','w')
#s=['aa\n','bb\n','cc\n']
#f.writelines(s)
#f.close()
'''
import  csv
p='test.csv'
c=csv.reader(open(p,'r',encoding='utf-8'))
for cs in c:
    print(cs[0])
'''
import  csv
fw= open('tt.csv','w')
c=csv.writer(fw)
dic ={"selenium":"se","appium":"aa"}
for key in dic:
    c.writerow([key,dic[key]])