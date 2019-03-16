from lesson_08.base import  base
class loginPage(base):
    def username(self):
        return self.by_id("nloginname")

    def passwd(self):
        return  self.by_id("npwd")

    def btn(self):
        return  self.by_id("nsubmit")

    def LoginIn(self,username,passwd):
        self.username().send_keys(username)
        self.passwd().send_keys(passwd)
        self.btn().click()
        return  self.dr_url()
