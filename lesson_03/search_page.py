
from lesson_03.com import driver,id,js,css,xpath
def search(leave,arrive,da):
    id(leave).send_keys("上海")
    css(arrive).send_keys("杭州")
    js(da)
    id(da).clear()
    id(da).send_keys("2019-01-05")


def train_No(m):
    css("#resultFilters01 > dl:nth-child(2) > dd:nth-child("+str(m)+") > label > i").click()

def train_num(s):
    xpath("//div[contains(@id,'tbody-01-" + s + "')]/div[1]/div[6]/div[1]/a").click()

