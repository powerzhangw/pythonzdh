from selenium import  webdriver
#path=r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
#path="C:\\Program Files (x86)\\Google\\Chrome\\chromedriver.exe"
path="C:/Program Files (x86)/Google/Chrome/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://www.baidu.com")