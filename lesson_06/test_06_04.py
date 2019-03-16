from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
driver = webdriver.Remote(
command_executor='http://127.0.0.1:4444/wd/hub',
desired_capabilities=DesiredCapabilities.CHROME)
driver.get("http://www.baidu.com")
driver.quit()



