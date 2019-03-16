from lesson_08.base import base
import  time
class noPage(base):
    #预定车票
    def book(self):
        return self.by_xpath("//*[@id='tbody-01-K5260']/div[1]/div[6]/div[1]/a")

    def book_close(self):
        return  self.by_css("#appd_wrap_close")

    def book_nologin(self):
        return  self.by_css("#btn_nologin")

    def bookBtn(self):
        self.book().click()
        time.sleep(2)
        self.book_close().click()
        time.sleep(2)
        self.book_nologin().click()