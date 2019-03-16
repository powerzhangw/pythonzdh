from selenium import webdriver
from selenium.webdriver.support.select import  Select
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome(path)
driver.get("https://passport.ctrip.com/user/reg/home")
driver.find_element_by_css_selector("#agr_pop > div.pop_footer > a.reg_btn.reg_agree").click()
time.sleep(3)
sour=driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-drop-btn")
print( sour.size['width'])
print(sour.size["height"])
ele=driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-bg-bar")
print( ele.size['width'])
print(ele.size["height"])
ActionChains(driver).drag_and_drop_by_offset(sour,ele.size['width'],-sour.size["height"]).perform()