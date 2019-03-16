
from lesson_03.com import driver,id,js,css,xpath
from lesson_03.com import  log
import  xlrd

def read_excel(filename,index,cloumn):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    data=[]
    for i in range(sheet.nrows):
        data.append(sheet.row_values(i)[0])
 #      print (sheet.row_values(i)[0])
    return  data


def search(leave,arrive,da):
    log("input leave city")
    id(leave).send_keys("上海")
    log("input arrive city")
    css(arrive).send_keys("杭州")
    log("input date")
    js(da)
    id(da).clear()
    id(da).send_keys("20190106")


def train_No(m):
    css("#resultFilters01 > dl:nth-child(2) > dd:nth-child("+str(m)+") > label > i").click()

def train_num(s):
    xpath("//div[contains(@id,'tbody-01-" + s + "')]/div[1]/div[6]/div[1]/a").click()

