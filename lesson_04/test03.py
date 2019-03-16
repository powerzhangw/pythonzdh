'''
import  json
js ={ "android":"appium","web":"selenium","interface":"requests" }
print(type(js))
print(type(json.dumps(js)))
print(type(json.loads(json.dumps(js))))
f =open("test.json",'r')
print(json.load(f))

f=open("tt.json",'w')
json.dump(js,f)
'''
import  xml.dom.minidom

dom=xml.dom.minidom.parse("user.xml")
root= dom.documentElement
ls=root.getElementsByTagName("user")
print(ls[0].getAttribute("id"))
print(ls[1].getElementsByTagName("password")[0].childNodes[0].nodeValue)
for l in ls:
    print(l.getElementsByTagName("password")[0].childNodes[0].nodeValue)