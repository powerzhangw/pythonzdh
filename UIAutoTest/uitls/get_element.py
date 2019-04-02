# #coding=utf-8
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# import sys
# # 定位
# def element(driver,method, location):
#     logs.info_log(u'获取定位'  + method + ':' + location)
#     time.sleep(0.5)
#     try:
#         if method == 'id':
#             element_wait(driver,method,location)
#             element = driver.find_element_by_id(location)
#         elif method == "name":
#             element_wait(driver, method, location)
#             element = driver.find_element_by_name(location)
#         elif method == "class":
#             element_wait(driver, method, location)
#             element = driver.find_element_by_class_name(location)
#         elif method == "link_text":
#             element_wait(driver, method, location)
#             element = driver.find_element_by_link_text(location)
#         elif method == "xpath":
#             element_wait(driver, method, location)
#             element = driver.find_element_by_xpath(location)
#         elif method == "tag":
#             element_wait(driver, method, location)
#             element = driver.find_element_by_tag_name(location)
#         elif method == "css":
#             element_wait(driver, method, location)
#             element = driver.find_element_by_css_selector(location)
#         else:
#             raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
#         return element
#     except Exception , e:
#         logs.error_log(e)
#
# # 组定位
# def elements(driver, method, location):
#     logs.info_log(u'获取定位' + method + ':' + location)
#     time.sleep(0.5)
#     try:
#         if method == 'id':
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_id(location)
#         elif method == "name":
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_name(location)
#         elif method == "class":
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_class_name(location)
#         elif method == "link_text":
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_link_text(location)
#         elif method == "xpath":
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_xpath(location)
#         elif method == "tag":
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_tag_name(location)
#         elif method == "css":
#             element_wait(driver, method, location)
#             element = driver.find_elements_by_css_selector(location)
#         else:
#             raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
#         return element
#     except Exception,e:
#         logs.error_log(e)
#
# # 等待
# def element_wait(driver, method, location, wati=6):
#     logs.info_log(u'正在查找元素' + method + ':' + location)
#     try:
#         if method == "id":
#             WebDriverWait(driver, wati, 1).until(EC.presence_of_element_located((By.ID, location)))
#         elif method == "name":
#             WebDriverWait(driver, wati, 1).until(EC.presence_of_element_located((By.NAME, location)))
#         elif method == "class":
#             WebDriverWait(driver, wati, 1).until(EC.presence_of_element_located((By.CLASS_NAME, location)))
#         elif method == "link_text":
#             WebDriverWait(driver, wati, 1).until(EC.presence_of_element_located((By.LINK_TEXT, location)))
#         elif method == "xpath":
#             WebDriverWait(driver, wati, 1).until(EC.presence_of_element_located((By.XPATH, location)))
#         elif method == "css":
#             WebDriverWait(driver, wati, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, location)))
#         else:
#             raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")
#     except Exception ,e:
#         logs.error_log(u'找不到元素超时')
#         logs.error_log(e)
#
# # 单击
# def clic(driver,method,location):
#     logs.info_log(u'点击定位元素' + method + ':' +location)
#     element_wait(driver,method, location)
#     e1 = element(driver,method, location)
#     e1.click()
#
# # 点击文字
# def click_text(driver, text):
#     logs.info_log(u'点击' +  text)
#     driver.find_element_by_link_text(text).click()
#
# # 截屏
# def get_screen(driver):
#     time_01 = time.ctime()
#     name = (time_01[-16:-5]).replace(':', '-')
#     logs.info_log(u'错误截屏')
#     driver.get_screenshot_as_file(config.picture_path() + '\\' + '%s'%name +".png")
#
# # 等待
# def wait(driver, method, location):
#     logs.info_log(u'定位元素' + method + ':' + location + u'正在等待中')
#     driver.implicitly_wait((method, location))
#
# # 切换
# def switch_to_frame(driver, method, location):
#     logs.info_log(u'切换到新的模态框定位元素' + method + ':' + location)
#     element_wait(driver,method,location)
#     if1 = element(driver,method, location)
#     driver.switch_to.frame(if1)
#
# #获取txt
# def get_text(driver, method, location):
#     element_wait(driver,method, location)
#     e1 = element(driver,method, location)
#     logs.info_log(u'获取到定位元素' + method + ':' + location + u'的文本为' + e1.text)
#     return e1.text
#
# #获取属性值
# def get_attribute(driver, method, location, attribute):
#     e1 = element(driver,method, location)
#     logs.info_log(u'获取到定位元素' + method + ':' + location + u'的属性为' + e1.get_attribute(attribute))
#     return e1.get_attribute(attribute)
#
# # 刷新
# def f5(driver):
#     logs.info_log(u'刷新当前页面')
#     driver.refresh()
#
# #文件上传
# def upfiles(driver,method, location,script_path):
#     logs.info_log(u'上传文件')
#     time.sleep(0.5)
#     clic(driver,method,location)
#     os.system(script_path)
#
# #下拉框
# def drow_down_input(driver,name,content):
#     logs.info_log(u'获取下拉框定位元素' + name + content)
#     time.sleep(1)
#     try:
#         if name == u'贷款产品':
#             if content == u'房贷一抵':
#                 xpath = '//*[@name="tSelectproductId"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'押车贷款（全款）':
#                 xpath = '//*[@name="tSelectproductId"]/div/div/div[2]/ul[2]/li[2]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'优车贷':
#                 xpath = '//*[@name="tSelectproductId"]/div/div/div[2]/ul[2]/li[3]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'资方主体':
#             if content == u'宜贷网（P2P资方）':
#                 xpath = '//*[@name="tSelectfunder"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'新网银行':
#                 xpath = '//*[@name="tSelectfunder"]/div/div/div[2]/ul[2]/li[2]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'外贸信托':
#                 xpath = '//*[@name="tSelectfunder"]/div/div/div[2]/ul[2]/li[3]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'金宝保':
#                 xpath = '//*[@name="tSelectfunder"]/div/div/div[2]/ul[2]/li[4]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'还款状态':
#             if content == u'在贷':
#                 xpath = '//*[@name="tSelectrepayStatus"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'已回购':
#                 xpath = '//*[@name="tSelectrepayStatus"]/div/div/div[2]/ul[2]/li[2]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'提前清贷':
#                 xpath = '//*[@name="tSelectrepayStatus"]/div/div/div[2]/ul[2]/li[3]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'正常清贷':
#                 xpath = '//*[@name="tSelectrepayStatus"]/div/div/div[2]/ul[2]/li[4]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'还款方式':
#             if content == u'等额本息':
#                 xpath = '//*[@name="tSelectmethod"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'等额本金':
#                 xpath = '//*[@name="tSelectmethod"]/div/div/div[2]/ul[2]/li[2]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'先息后本':
#                 xpath = '//*[@name="tSelectmethod"]/div/div/div[2]/ul[2]/li[3]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'等本等息':
#                 xpath = '//*[@name="tSelectmethod"]/div/div/div[2]/ul[2]/li[4]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'债券状态':
#             if content == u'正常':
#                 xpath = '//*[@name="tSelectisAdvance"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'垫付':
#                 xpath = '//*[@name="tSelectisAdvance"]/div/div/div[2]/ul[2]/li[2]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'受让':
#                 xpath = '//*[@name="tSelectisAdvance"]/div/div/div[2]/ul[2]/li[3]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'所属大区':
#             if content == u'暴力街区':
#                 xpath = '//*[@name="tSelectarea"]/div/div/div[2]/ul[2]/li[5]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'所属城市':
#             if content == u'成都':
#                 xpath = '//*[@name="tSelectCity"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'所属部门':
#             if content == u'测试部':
#                 xpath = '//*[@name="tSelectDeptName"]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'成都房贷一部':
#                 xpath = '//*[@name="tSelectDeptName"]/div/div/div[2]/ul[2]/li[3]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'产品部':
#                 xpath = '//*[@name="tSelectDeptName"]/div/div/div[2]/ul[2]/li[5]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'认领类型':
#             driver.find_element_by_xpath('//*[@name="tFormClaimManageClaim"]/div[9]/div/div/div[1]/div/span').click()
#             if content == u'正常':
#                 xpath = '//*[@name="tFormClaimManageClaim"]/div[9]/div/div/div[2]/ul[2]/li[1]'
#                 driver.find_element_by_xpath(xpath).click()
#             elif content == u'逾期':
#                 xpath = '//*[@name="tFormClaimManageClaim"]/div[9]/div/div/div[2]/ul[2]/li[2]'
#                 driver.find_element_by_xpath(xpath).click()
#         elif name == u'银行卡主要用途':
#             driver.find_element_by_name('tSelecttype').click()
#             if content == u'全部':
#                 driver.find_element_by_xpath('//*[@name="tSelecttype"]/div/div/div[2]/ul[2]/li[1]').click()
#             elif content == u'放款':
#                 driver.find_element_by_xpath('//*[@name="tSelecttype"]/div/div/div[2]/ul[2]/li[2]').click()
#             elif content == u'还款':
#                 driver.find_element_by_xpath('//*[@name="tSelecttype"]/div/div/div[2]/ul[2]/li[3]').click()
#         elif name == u'银行卡账户类型':
#             driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[3]/div/div/div[1]/div/span').click()
#             # driver.find_element_by_xpath('//*[@name="tSelectaccountTypeId"]/div/div/div[1]/div/span').click()
#             if content == u'个人账户':
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[3]/div/div/div[2]/ul[2]/li[1]').click()
#             elif content == u'企业账户':
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[3]/div/div/div[2]/ul[2]/li[2]').click()
#         elif name == u'银行卡证件类型':
#             driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[5]/div/div/div[1]/div/span').click()
#             if content == u'身份证':
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[5]/div/div/div[2]/ul[2]/li[1]').click()
#             elif content == u'户口簿':
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[5]/div/div/div[2]/ul[2]/li[2]').click()
#             else:
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[5]/div/div/div[2]/ul[2]/li[1]').click()
#         elif name == u'银行卡分支行':
#             if content == u'默认':
#                 #当为默认时，选择为“北京市-市辖区-招商银行北京分行"
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[9]/div/div/div[1]/div/span').click()
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[9]/div/div/div[2]/ul[2]/li[1]').click()
#                 time.sleep(0.5)
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[10]/div/div/div[1]/div/span').click()
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[10]/div/div/div[2]/ul[2]/li').click()
#                 time.sleep(0.5)
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[11]/div/div/div[1]/div/span').click()
#                 driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[11]/div/div/div[2]/ul[2]/li[1]').click()
#
#
#
#
#     except Exception,e:
#         logs.error_log(e)
#
# def page_enter(driver,page_name):
#     #输入需要进入的目录，进入对应的列表
#     logs.info_log(u'进入页面-' + page_name)
#     time.sleep(1)
#     # 先点击客户管理，然后再点击客户列表；
#     try:
#         if page_name == u'客户列表':
#             driver.find_element_by_id('tTopMenucustomer').click()
#             driver.find_element_by_id("tSideMenucustomerList").click()
#         elif page_name == u'在贷客户':
#             driver.find_element_by_id('tTopMenucustomer').click()
#             driver.find_element_by_id("tSideMenuloanList").click()
#         elif page_name == u'待还列表':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_xpath('//*[@id="tSideMenudeduct"]/div/span').click()
#             driver.find_element_by_id("tSideMenudeductdeduct-index").click()
#         elif page_name == u'划扣列表':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenudeduct").click()
#             driver.find_element_by_id("tSideMenudeductdeduct-deductList").click()
#         elif page_name == u'历史划扣':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenudeduct").click()
#             driver.find_element_by_id("tSideMenudeductdeduct-historyList").click()
#         elif page_name == u'转账客户':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenudeduct").click()
#             driver.find_element_by_id("tSideMenudeductdeduct-transferList").click()
#         elif page_name == u'认领列表':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenuclaim").click()
#             driver.find_element_by_id("tSideMenuclaimclaim-index").click()
#         elif page_name == u'历史认领':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenuclaim").click()
#             driver.find_element_by_id("tSideMenuclaimclaim-historyList").click()
#         elif page_name == u'回退审批':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenuclaim").click()
#             driver.find_element_by_id("tSideMenuclaimclaim-approvalList").click()
#         elif page_name == u'回盘流水导入':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenuclaim").click()
#             driver.find_element_by_id("tSideMenuclaimclaim-importList").click()
#         elif page_name == u'历史回盘':
#             driver.find_element_by_id("tTopMenurepayment").click()
#             driver.find_element_by_id("tSideMenuclaim").click()
#             driver.find_element_by_id("tSideMenuclaimclaim-historyBack").click()
#         elif page_name == u'客户卡管理':
#             driver.find_element_by_id("tTopMenubankcard").click()
#             driver.find_element_by_id("tSideMenuborrowerBank").click()
#     except Exception,e:
#         logs.error_log(e)
#
# #订单编号
# def number_clic(driver,number):
#     logs.info_log(u'正在查找订单编号' + number)
#     time.sleep(0.5)
#     try:
#         number_clic_xpath = "//*[text()= " + number + "]"
#         driver.find_element_by_xpath(number_clic_xpath).click()
#     except Exception ,e:
#         logs.error_log(e)
#
# #测试驱动路径及启动
# def test_driver(browsers):
#     logs.info_log(u'启动webdriver')
#     try:
#         if browsers == 'chrome' or browsers == 'Chrome' or browsers == 'c' or browsers == 'C':
#             driver_path = './drivers/chromedriver.exe'
#             browser = webdriver.Chrome(executable_path=driver_path)
#             return browser
#         elif browsers == 'firfox' or browsers == 'Firfox' or browsers == 'F' or browsers == 'f':
#             driver_path = './drivers/geckodriver.exe'
#             browser = webdriver.Firefox(executable_path=driver_path)
#             return browser
#         elif browsers == 'PhantomJS' or browsers =='phantomJS' or browsers == 'p' or browsers == 'P':
#             driver_path = './drivers/PhantomJS.exe'
#             browser = webdriver.PhantomJS(executable_path=driver_path)
#             return browser
#         else:
#             raise NameError(u'目前只支持firefox,Chrome,PhantomJS')
#     except Exception,e:
#         logs.error_log(e)
#
# #还款计划表-三张表数据
# def get_payment_datas(browsers,table_name):
#     if table_name == u'借款人表':
#         time.sleep(1)
#         #点击还款管理表按钮，进入还款管理页面
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[3]').click()
#         #点击“易捷表”，然后再点击“借款人表”
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[2]/div[2]/div/div[1]/div[2]').click()
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[2]/div[2]/div/div[1]/div[1]').click()
#         # 借款人表，所有行（应还、实还行）均展开
#         time.sleep(1)
#         for i in range(12,0,-1):
#             browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[1]/div/div/i'%i).click()
#             list_key = []
#             list_value_yh = []
#         for i in range(1,13):
#             list_key.append(u'第%s期-本期合计应还款额'%i)
#             list_key.append(u'第%s期-本期应还本息' % i)
#             list_key.append(u'第%s期-本期应还本金' % i)
#             list_key.append(u'第%s期-本期应还利息' % i)
#             list_key.append(u'第%s期-本期应还信息服务费期收' % i)
#             list_key.append(u'第%s期-本期应还信息服务费逾还' % i)
#             list_key.append(u'第%s期-当前还款状态' % i)
#             list_key.append(u'第%s期-本期合计实还款额' % i)
#             list_key.append(u'第%s期-本期实还本息' % i)
#             list_key.append(u'第%s期-本期实还本金' % i)
#             list_key.append(u'第%s期-本期实还利息' % i)
#             list_key.append(u'第%s期-本期实还信息服务费-期收' % i)
#             list_key.append(u'第%s期-本期实还信息服务费-逾还' % i)
#         for i in range(1,24,2):
#             bqhjyhke_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[4]/div/span' % i).text  # '''本期合计应还款额'''
#             list_value_yh.append(bqhjyhke_money)
#             bqysbx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[5]/div/span' % i).text  # '''本期应还本息'''
#             list_value_yh.append(bqysbx_money)
#             bqysbj_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[6]/div/span' % i).text  # '''本期应还本金'''
#             list_value_yh.append(bqysbj_money)
#             bqyslx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[7]/div/span' % i).text  # '''本期应还利息'''
#             list_value_yh.append(bqyslx_money)
#             bqysxxfwfqs_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[10]/div/span' % i).text  # '''本期应还信息服务费期收'''
#             list_value_yh.append(bqysxxfwfqs_money)
#             bqysxxfwfyq_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[11]/div/span' % i).text  # '''本期应还信息服务费逾还'''
#             list_value_yh.append(bqysxxfwfyq_money)
#             dqhkzt_type = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[12]/div/span' % i).text  # '''当前还款状态'''
#             list_value_yh.append(dqhkzt_type)
#             j = i + 1
#             bqhjyhke_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[2]/div/span' % j).text  # '''本期合计应还款额'''
#             list_value_yh.append(bqhjyhke_money)
#             bqysbx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[3]/div/span' % j).text  # '''本期应还本息'''
#             # bqysbx_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[3]/div/span' % j).text  # '''本期应还本息'''
#             list_value_yh.append(bqysbx_money)
#             bqysbj_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/span' % j).text  # '''本期应还本金'''
#             # bqysbj_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[4]/div/span' % j).text  # '''本期应还本金'''
#             list_value_yh.append(bqysbj_money)
#             bqyslx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[5]/div/span' % j).text  # '''本期应还利息'''
#             # bqyslx_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[5]/div/span' % j).text  # '''本期应还利息'''
#             list_value_yh.append(bqyslx_money)
#             bqysxxfwfqs_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[8]/div/span' % j).text  # '''本期应还信息服务费期收'''
#             # bqysxxfwfqs_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[8]/div/span' % j).text  # '''本期应还信息服务费期收'''
#             list_value_yh.append(bqysxxfwfqs_money)
#             bqysxxfwfyq_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[9]/div/span' % j).text  # '''本期应还信息服务费逾还'''
#             # bqysxxfwfyq_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[9]/div/span' % j).text  # '''本期应还信息服务费逾还'''
#             list_value_yh.append(bqysxxfwfyq_money)
#         for i in range(156):
#             dict_01 = dict(zip(list_key,list_value_yh))
#             return (dict_01)
#
#     elif table_name == u'易捷表':
#         time.sleep(1)
#         # 点击还款管理表按钮，进入还款管理页面
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[3]').click()
#         # 点击“借款人表”，然后再点击“易捷表”
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[2]/div[2]/div/div[1]/div[1]').click()
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[2]/div[2]/div/div[1]/div[2]').click()
#         # 易捷表，所有行（应还、实还行）均展开
#         time.sleep(1)
#         for i in range(12, 0, -1):
#             browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[1]/div/div/i' % i).click()
#             list_key = []
#             list_value_yh = []
#         for i in range(1, 13):
#             list_key.append(u'第%s期-本期合计应收款额' % i)
#             list_key.append(u'第%s期-本期应收代收代付资方本息费' % i)
#             list_key.append(u'第%s期-本期应收垫付本息费' % i)
#             list_key.append(u'第%s期-本期应收垫付本金' % i)
#             list_key.append(u'第%s期-本期应收服务费总额' % i)
#             list_key.append(u'第%s期-本期应收信息服务费-期收' % i)
#             list_key.append(u'第%s期-本期应收信息服务费-逾还' % i)
#             list_key.append(u'第%s期-本期合计实收款额' % i)
#             list_key.append(u'第%s期-本期实收代收代付资方本息费' % i)
#             list_key.append(u'第%s期-本期实收垫付本息费' % i)
#             list_key.append(u'第%s期-本期实收垫付本金' % i)
#             list_key.append(u'第%s期-本期实收服务费总额' % i)
#             list_key.append(u'第%s期-本期应收信息服务费-期收' % i)
#         for i in range(1, 24, 2):
#             bqhjyhke_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[4]/div/span' % i).text  # '''本期合计应收款额'''
#             list_value_yh.append(bqhjyhke_money)
#             bqysbx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[5]/div/span' % i).text  # '''本期应收代收代付资方本息费'''
#             list_value_yh.append(bqysbx_money)
#             bqysbj_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[6]/div/span' % i).text  # '''本期应收垫付本息费'''
#             list_value_yh.append(bqysbj_money)
#             bqyslx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[7]/div/span' % i).text  # '''本期应收垫付本金'''
#             list_value_yh.append(bqyslx_money)
#             bqysxxfwfqs_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[10]/div/span' % i).text  # '''本期应收服务费总额'''
#             list_value_yh.append(bqysxxfwfqs_money)
#             bqysxxfwfyq_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[11]/div/span' % i).text  # '''本期应收信息服务费-期收'''
#             list_value_yh.append(bqysxxfwfyq_money)
#             dqhkzt_type = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[12]/div/span' % i).text  # '''本期应收信息服务费-逾还'''
#             list_value_yh.append(dqhkzt_type)
#             j = i + 1
#             bqhjyhke_money = browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[2]/div/span' % j).text  # '''本期合计应还款额'''
#             list_value_yh.append(bqhjyhke_money)
#             bqysbx_money = browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[3]/div/span' % j).text  # '''本期应还本息'''
#             # bqysbx_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[3]/div/span' % j).text  # '''本期应还本息'''
#             list_value_yh.append(bqysbx_money)
#             bqysbj_money = browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/span' % j).text  # '''本期应还本金'''
#             # bqysbj_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[4]/div/span' % j).text  # '''本期应还本金'''
#             list_value_yh.append(bqysbj_money)
#             bqyslx_money = browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[5]/div/span' % j).text  # '''本期应还利息'''
#             # bqyslx_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[5]/div/span' % j).text  # '''本期应还利息'''
#             list_value_yh.append(bqyslx_money)
#             bqysxxfwfqs_money = browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[8]/div/span' % j).text  # '''本期应还信息服务费期收'''
#             # bqysxxfwfqs_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[8]/div/span' % j).text  # '''本期应还信息服务费期收'''
#             list_value_yh.append(bqysxxfwfqs_money)
#             bqysxxfwfyq_money = browsers.find_element_by_xpath(
#                 '//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[9]/div/span' % j).text  # '''本期应还信息服务费逾还'''
#             # bqysxxfwfyq_money = driver.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[1]/table/thead/tr/th[9]/div/span' % j).text  # '''本期应还信息服务费逾还'''
#             list_value_yh.append(bqysxxfwfyq_money)
#         for i in range(156):
#             dict_01 = dict(zip(list_key, list_value_yh))
#             return (dict_01)
#
#     elif table_name == u'资方表':
#         time.sleep(1)
#         # 点击还款管理表按钮，进入还款管理页面
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[3]').click()
#         # 点击“借款人表”，然后再点击“资方表”
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[2]/div[2]/div/div[1]/div[1]').click()
#         browsers.find_element_by_xpath('//*[@class="detailItem2"]/div/div[2]/div[2]/div/div[1]/div[3]').click()
#         # 易捷表，所有行（应还、实还行）均展开
#         time.sleep(1)
#         for i in range(12, 0, -1):
#             browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[1]/div/div/i' % i).click()
#             list_key = []
#             list_value_yh = []
#         for i in range(1, 13):
#             list_key.append(u'第%s期-本期合计应还款额' % i)
#             list_key.append(u'第%s期-本期应还本息' % i)
#             list_key.append(u'第%s期-本期应还本金' % i)
#             list_key.append(u'第%s期-本期应还利息' % i)
#             list_key.append(u'第%s期-本期应还逾期罚息' % i)
#             list_key.append(u'第%s期-本期应还资方服务费' % i)
#             list_key.append(u'第%s期-当前还款状态' % i)
#             list_key.append(u'第%s期-本期合计实还款额' % i)
#             list_key.append(u'第%s期-本期实还本息' % i)
#             list_key.append(u'第%s期-本期实还本金' % i)
#             list_key.append(u'第%s期-本期实还利息' % i)
#             list_key.append(u'第%s期-本期实还逾期罚息' % i)
#             list_key.append(u'第%s期-本期实还资方服务费' % i)
#         for i in range(1, 24, 2):
#             bqhjyhke_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[4]/div/span' % i).text  # '''本期合计应还款额'''
#             list_value_yh.append(bqhjyhke_money)
#             bqysbx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[5]/div/span' % i).text  # '''本期应还本息'''
#             list_value_yh.append(bqysbx_money)
#             bqysbj_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[6]/div/span' % i).text  # '''本期应还本金'''
#             list_value_yh.append(bqysbj_money)
#             bqyslx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[7]/div/span' % i).text  # '''本期应还利息'''
#             list_value_yh.append(bqyslx_money)
#             bqysxxfwfqs_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[8]/div/span' % i).text  # '''本期应还逾期罚息'''
#             list_value_yh.append(bqysxxfwfqs_money)
#             bqysxxfwfyq_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[10]/div/span' % i).text  # '''本期应还资方服务费'''
#             list_value_yh.append(bqysxxfwfyq_money)
#             dqhkzt_type = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td[11]/div/span' % i).text  # '''当前还款状态'''
#             list_value_yh.append(dqhkzt_type)
#             j = i + 1
#             bqhjyhke_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[2]/div/span' % j).text  # '''本期合计应还款额'''
#             list_value_yh.append(bqhjyhke_money)
#             bqysbx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[3]/div/span' % j).text  # '''本期应还本息'''
#             list_value_yh.append(bqysbx_money)
#             bqysbj_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/span' % j).text  # '''本期应还本金'''
#             list_value_yh.append(bqysbj_money)
#             bqyslx_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[5]/div/span' % j).text  # '''本期应还利息'''
#             list_value_yh.append(bqyslx_money)
#             bqysxxfwfqs_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[6]/div/span' % j).text  # '''本期应还信息服务费期收'''
#             list_value_yh.append(bqysxxfwfqs_money)
#             bqysxxfwfyq_money = browsers.find_element_by_xpath('//*[@name="tTableCustomerDetail"]/div/div[2]/table/tbody/tr[%s]/td/div/div/div/div/div[2]/table/tbody/tr/td[8]/div/span' % j).text  # '''本期应还信息服务费逾还'''
#             list_value_yh.append(bqysxxfwfyq_money)
#         for i in range(156):
#             dict_01 = dict(zip(list_key, list_value_yh))
#             return (dict_01)
#
# # 进入订单详情页
# def order_details_page(driver,order_num):
#     logs.info_log(u'进入订单详情页')
#     time.sleep(1)
#     try:
#         driver.find_element_by_id('tTopMenucustomer').click()
#         driver.find_element_by_id('tSideMenuloanList').click()
#         driver.find_element_by_name('tInputFilter').clear()
#         driver.find_element_by_name('tInputFilter').send_keys(order_num)
#         driver.find_element_by_name('tBtnFilter').click()
#         time.sleep(0.5)
#         number_clic_xpath = "//*[text()= " + order_num + "]"
#         driver.find_element_by_xpath(number_clic_xpath).click()
#     except Exception,e:
#         logs.error_log(e)
#
# # 根据客户名获取订单编号；
# def order_sn_id(driver,order_name):
#     logs.info_log(u'获取' + order_name + u'的订单ID')
#     time.sleep(1)
#     try:
#         driver.find_element_by_id('tTopMenucustomer').click()
#         driver.find_element_by_id('tSideMenuloanList').click()
#         driver.find_element_by_name('tInputFilter').clear()
#         driver.find_element_by_name('tInputFilter').send_keys(u'%s'%order_name)
#         driver.find_element_by_name('tBtnFilter').click()
#         time.sleep(0.5)
#         order_id = driver.find_element_by_xpath('//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr/td[1]/div/a').text
#         return order_id
#     except Exception,e:
#         logs.error_log(e)
#
# #关闭其他页签或全部页签；
# def close_all_tab(driver,text):
#     logs.info_log(u'关闭其他页签或全部页签')
#     if text == 'all':
#         try:
#             time.sleep(5)
#             driver.find_element_by_xpath('//*[@class="close-all-tag-con"]/div/div/button/span').click()
#             time.sleep(1)
#             driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]').click()
#             time.sleep(3)
#         except Exception,e:
#             logs.error_log(e)
#     else:
#         try:
#             driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/button/span').click()
#             time.sleep(0.5)
#             driver.find_element_by_xpath('/html/body/div[3]/ul/li[2]').click()
#             time.sleep(3)
#         except Exception,e:
#             logs.error_log(e)
#
# #补充银行卡信息，便于划扣成功；
# def edit_bankcard(driver):
#     logs.info_log(u'补充银行卡相关信息')
#     pass
