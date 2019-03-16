from selenium import webdriver
import time
from lesson_03.com import id,js

path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://trains.ctrip.com/TrainBooking/Search.aspx?from=shanghai&to=hangzhou&day=2019-01-03&number=&fromCn=%25E4%25B8%258A%25E6%25B5%25B7&toCn=%25E6%259D%25AD%25E5%25B7%259E')
#m =9
#driver.find_element_by_css_selector("#resultFilters01 > dl:nth-child(2) > dd:nth-child("+str(m)+") > label > i").click()
#driver.find_element_by_xpath("//*[@id='tbody-01-K18050']/div[1]/div[6]/div[1]/a").click()
time.sleep(6)
#driver.find_element_by_xpath("//div[starts-with(@id,'tbody-01-K1805')]/div[1]/div[6]/div[1]/a").click()
s='K1805'
driver.find_element_by_xpath("//div[contains(@id,'tbody-01-"+s+"')]/div[1]/div[6]/div[1]/a").click()
