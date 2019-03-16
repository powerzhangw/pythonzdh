from selenium import webdriver
from selenium.webdriver.support.select import  Select
path= 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
from selenium.webdriver.common.action_chains import ActionChains
import  time
from PIL import Image
driver = webdriver.Chrome(path)
driver.get("https://pan.baidu.com/")
'''
time.sleep(20)
cookies=driver.get_cookies()
print(cookies)
'''
coo =[{'domain': '.baidu.com', 'expiry': 1577880662.270573, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '5F2BEFF36DF2066CD41FC1A0B683FC6A:FG=1'}, {'domain': '.baidu.com', 'expiry': 1805544677.78773, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'dzcy15bTlwclBCM2k3NWc4UW9WeEswa3lvTlZVR1BmSG5zSFRnYXpCaFVUVWxjQVFBQUFBJCQAAAAAAAAAAAEAAACfsRPqsK7QprXExa7J-jk2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTAIVxUwCFcNE'}, {'domain': '.pan.baidu.com', 'expiry': 1548936679.568986, 'httpOnly': True, 'name': 'SCRC', 'path': '/', 'secure': False, 'value': '175fc92046e82fe69c6bf7e3136ccce0'}, {'domain': 'pan.baidu.com', 'expiry': 4138344678.879698, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.pan.baidu.com', 'expiry': 1546431082.000784, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '7510796547527406518%3AlerdBBtX5a8cdsRZ0BVdhOn90oj%2BY%2FIssQ%2F0m%2FxncDQZTC6F31NtRNFLhumo1Yci7UGb%2BBwsnzlKu8WyLCLL4euXvJ%2Fh0Blj2JnHdAqj4cpTefW8aCRF9VfUDd9arCIiMKyNsrzXlkZ9ZcgdTWZcl2NtiaXV6jA2rsgnNL%2BLYct9tn9thbnTpv7IiW4JizVanZlv3sbf6BI%3D'}, {'domain': '.pan.baidu.com', 'expiry': 1577880679.022701, 'httpOnly': False, 'name': 'PANWEB', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.pan.baidu.com', 'expiry': 1577880680, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1546344681'}, {'domain': '.pan.baidu.com', 'expiry': 1548936679.568947, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': 'd19d2b84429e152fd7f439acb853127b004eb97135c551f1db660f850d2aaba5'}, {'domain': '.pan.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1546344681'}, {'domain': '.baidu.com', 'expiry': 1547208711, 'httpOnly': False, 'name': 'cflag', 'path': '/', 'secure': False, 'value': '13%3A3'}]

for cookie in coo:
    driver.add_cookie(cookie)
time.sleep(5)
driver.get("https://pan.baidu.com/")