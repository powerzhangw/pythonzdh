from pywinauto.application import  Application
import time
app =Application()
app = app.connect(title_re="打开",class_name="#32770")
app['打开']["EDit1"].SetEditText("C:\Users\Administrator\Desktop\11.txt")
time.sleep(2)
app["打开"]["Button1"].click()

print("end")