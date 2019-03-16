from selenium import webdriver
import  xlrd
import  logging
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
driver = webdriver.Chrome(path)

def log(str):
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log-selenium.log',
                    filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)
'''
def id(driver,ele):
    return driver.find_element_by_id(ele)

def js(driver,ele):
    driver.execute_script("document.getElementById("+"'"+ele+"'"+").removeAttribute('readonly')")
#    print("document.getElementById("+"'"+ele+"'"+").removeAttribute('readonly')")

'''
#id
def id(ele):
    return driver.find_element_by_id(ele)
#css
def css(ele):
    return driver.find_element_by_css_selector(ele)

def js(ele):
    driver.execute_script("document.getElementById("+"'"+ele+"'"+").removeAttribute('readonly')")

def xpath(ele):
    return  driver.find_element_by_xpath(ele)

def search(leave,arrive,da):
    id(leave).send_keys("上海")
    css(arrive).send_keys("杭州")
    js(da)
    id(da).clear()
    id(da).send_keys("2019-01-05")

def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    dic={}
    for j in range(sheet.ncols):

        data=[]
        for i in range(sheet.nrows):
          data.append(sheet.row_values(i)[j])
        dic[j]=data
    return  dic