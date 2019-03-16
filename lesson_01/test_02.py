from selenium import webdriver
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
import  time
driver = webdriver.Chrome(path)
driver.get('https://passport.meituan.com/account/unitivelogin?')
driver.maximize_window()
#driver.find_element_by_id('login-email').send_keys('test')
time.sleep(2)
#driver.find_element_by_id('login-email').clear()
'''
print (driver.find_element_by_id('login-email').is_displayed())
print(driver.find_element_by_id('login-email').is_enabled())
print(driver.find_element_by_id('login-email').is_selected())

print(driver.current_url)
print(driver.current_window_handle)

#print(driver.find_element_by_link_text('免费注册').text)

driver.back()
driver.forward()
'''
driver.quit()