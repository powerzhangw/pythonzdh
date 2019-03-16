from lesson_08.base import  base
import  time
class searchPage(base):
    def search_leave(self):
        return self.by_id("notice01")

    def search_arrive(self):
        return  self.by_css("#notice08")

    def search_date(self):
        return  self.by_id("dateObj")

    def search_btn(self):
        return  self.by_id("searchbtn")

    def search_current(self):
        return  self.by_css("#searchtype > li.current")

    def search_js(self,value):
        jsvalue="document.getElementById('dateObj').value='%s'"%(value)
        return self.driver.execute_script(jsvalue)

    def Search_Train(self,leave,arrive,leave_date):
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        self.search_js(leave_date)
        self.search_current().click()
        self.search_btn().click()
        time.sleep(4)
        return  self.dr_url()
