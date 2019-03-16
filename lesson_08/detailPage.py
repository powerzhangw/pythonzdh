from lesson_08.base import base
import  time
class detailPage(base):
    #预定车票
    def detail_name(self):
        return self.by_css("#pasglistdiv > div > ul > li:nth-child(2) > input")



    def detail_name(self,name):
        self.detail_name().send_keys(name)
        time.sleep(2)
