#coding=utf-8
import urllib
import urllib2
import random
import string
import time
import json
import sys
reload(sys)
import sys,time,datetime,random
reload(sys)
sys.setdefaultencoding('utf8')
a = '111'
b = '222'
print('%s,11111111111111111111111%s'%(a,b))




# def deduction_money(self,ID,claim_money,zifang,hklx=None,czuo=u'划扣'):
#     try:
#         #关闭所有标签
#         get_element.close_all_tab(self.browser,text='all')
#         # 进入划扣列表
#         get_element.page_enter(self.browser, u'待还列表')
#         if zifang == u'易捷' and hklx == u'正常待还' and czuo == u'划扣':
#             # 进入划扣页面-点击待还列表按钮
#             self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
#             # 进入划扣页面-点击易捷按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
#             # 进入划扣页面-点击正常待还按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_normalrepaymentpath)
#             # 根据id查询出订单
#             self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).clear()
#             self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).send_keys('%s'%ID)
#             self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_confirmname)
#             # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
#             # 验证应还总额是否正确，等于贷前费用；
#             yhze_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yh_money)
#             # 验证预还款额是否正确,是否为0；
#             yhkje_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_money)
#             # 验已还款额是否正确，是否为0；
#             yhke_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_hk_money)
#             # 点击划扣按钮,输入划扣金额；
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_deductionpath)
#             # self.logs.info_log(u'还款管理页面，进入划扣页面，划扣金额，验证划扣是否成功；')
#             self.driver.element(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_xpath).clear()
#             self.driver.element(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_xpath).send_keys('%s'%claim_money)
#             # 选择划扣时间为当前日期；
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_hksj_xpath)
#             self.driver.element(self.browser, 'xpath', payment_deduction.wait_repayment_hksj_xpath).send_keys(Keys.ENTER)
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_hksj_button_xpath)
#             # 账户选择下拉框，选择对应的账户；
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zhhm_xpath)
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zhhm_xpath_01)
#             # 划扣确认页面，点击确定按钮,验证提示“划扣成功”
#             self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_submit_name)
#             hkjg = self.driver.get_text(self.browser,'xpath', '//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
#             time.sleep(7)
#             return {u'应还总额':yhze_money,u'预划扣额':yhkje_money,u'已还款额':yhke_money,u'划扣结果':hkjg}
#         elif zifang == u'易捷' and hklx == u'逾期待还'and czuo == u'划扣':
#             # 进入划扣页面-点击待还列表按钮
#             self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
#             # 进入划扣页面-点击易捷按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
#             # 进入划扣页面-点击逾期待还按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_overduerepaymentpath)
#             # 根据id查询出订单
#             self.driver.element(self.browser, 'xpath',
#                                 '//div[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
#             self.driver.element(self.browser, 'xpath', '//div[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'%ID)
#             self.driver.clic(self.browser, 'xpath', '//div[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[1]/form/div[6]/div/button[1]/span')
#             # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
#             # 验证应还总额是否正确，等于贷前费用；
#             yhze_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[7]/div/span')
#             # 验证预还款额是否正确,是否为0；
#             yhkje_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div/span')
#             # 验已还款额是否正确，是否为0；
#             yhke_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/span')
#             # 点击划扣按钮,输入划扣金额；
#             self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[1]')
#             # self.logs.info_log(u'还款管理页面，进入划扣页面，划扣金额，验证划扣是否成功；')
#             self.driver.element(self.browser, 'xpath','/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/input').clear()
#             self.driver.element(self.browser, 'xpath','/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys('%s'%claim_money)
#             # 选择划扣时间为当前日期；
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input')
#             self.driver.element(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/div/div/div/div[4]/button[3]/span')
#             # 账户选择下拉框，选择对应的账户；
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/div[1]/div/span')
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li')
#             # 划扣确认页面，点击确定按钮,验证提示“划扣成功”
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[3]/div/button[2]')
#             hkjg = self.driver.get_text(self.browser, 'xpath', '//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
#             time.sleep(7)
#             return {u'应还总额':yhze_money,u'预划扣额':yhkje_money,u'已还款额':yhke_money,u'划扣结果':hkjg}
#         elif zifang == u'资方' and hklx == None and czuo == u'划扣':
#             # 进入划扣页面-点击待还列表按钮
#             self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
#             # 进入划扣页面-点击资方按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zfpath)
#             # 根据id查询出订单
#             self.driver.element(self.browser, 'xpath',
#                                 '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
#             self.driver.element(self.browser, 'xpath', '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'%ID)
#             self.driver.clic(self.browser, 'xpath', '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/form/div[6]/div/button[1]')
#             # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
#             # 验证应还总额是否正确，等于贷前费用；
#             yhze_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[7]/div/span')
#             # 验证预还款额是否正确,是否为0；
#             yhkje_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[8]/div/span')
#             # 验已还款额是否正确，是否为0；
#             yhke_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[9]/div/span')
#             # 点击划扣按钮,输入划扣金额；
#             self.driver.clic(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[10]/div/div/a[1]')
#             # self.logs.info_log(u'还款管理页面，进入划扣页面，划扣金额，验证划扣是否成功；')
#             self.driver.element(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[3]/div/div/input').clear()
#             self.driver.element(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys('%s'%claim_money)
#             # 选择划扣时间为当前日期；
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input')
#             self.driver.element(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input').send_keys(
#                 Keys.ENTER)
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/div/div/div/div[4]/button[3]/span')
#             # 账户选择下拉框，选择对应的账户；
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[5]/div/div/div[1]/div/span')
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li')
#             # 划扣确认页面，点击确定按钮,验证提示“划扣成功”
#             self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[3]/div/button[2]/span')
#             hkjg = self.driver.get_text(self.browser, 'xpath', '//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
#             time.sleep(7)
#             return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
#         elif zifang == u'易捷' and hklx == u'正常待还' and czuo == u'转账':
#             # 进入划扣页面-点击待还列表按钮
#             self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
#             # 进入划扣页面-点击易捷按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
#             # 进入划扣页面-点击正常待还按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_normalrepaymentpath)
#             # 根据id查询出订单
#             self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).clear()
#             self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).send_keys('%s'%ID)
#             self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_confirmname)
#             # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
#             # 验证应还总额是否正确，等于贷前费用；
#             yhze_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yh_money)
#             # 验证预还款额是否正确,是否为0；
#             yhkje_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_money)
#             # 验已还款额是否正确，是否为0；
#             yhke_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_hk_money)
#             # 点击转账按钮，进入转账页面；
#             self.driver.clic(self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
#             self.driver.clic(self.browser,'xpath','//*[@class="ivu-modal-content"]/div/div/div[3]/button[2]/span')
#             hkjg = self.driver.get_text(self.browser, 'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
#             time.sleep(7)
#             return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
#         elif zifang == u'易捷' and hklx == u'逾期待还' and czuo == u'转账':
#             # 进入划扣页面-点击待还列表按钮
#             self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
#             # 进入划扣页面-点击易捷按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
#             # 进入划扣页面-点击正常待还按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_normalrepaymentpath)
#             # 根据id查询出订单
#             self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).clear()
#             self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).send_keys('%s'%ID)
#             self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_confirmname)
#             # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
#             # 验证应还总额是否正确，等于贷前费用；
#             yhze_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yh_money)
#             # 验证预还款额是否正确,是否为0；
#             yhkje_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_money)
#             # 验已还款额是否正确，是否为0；
#             yhke_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_hk_money)
#             # 点击转账按钮，进入转账页面；
#             self.driver.clic(self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
#             self.driver.clic(self.browser,'xpath','//*[@class="ivu-modal-content"]/div/div/div[3]/button[2]/span')
#             hkjg = self.driver.get_text(self.browser, 'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
#             time.sleep(7)
#             return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
#         elif zifang == u'资方' and hklx == None and czuo == u'转账':
#             # 进入划扣页面-点击待还列表按钮
#             self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
#             # 进入划扣页面-点击资方按钮
#             self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zfpath)
#             # 根据id查询出订单
#             self.driver.element(self.browser, 'xpath',
#                                 '//*[@name="tTagDeductWait"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
#             self.driver.element(self.browser, 'xpath', '//*[@name="tTagDeductWait"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'%ID)
#             self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductWait"]/div[2]/div[2]/div/div[1]/form/div[6]/div/button[1]')
#             # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
#             # 验证应还总额是否正确，等于贷前费用；
#             yhze_money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[7]/div/span')
#             # 验证预还款额是否正确,是否为0；
#             yhkje_money = self.driver.get_text(self.browser, 'xpath',
#                                                '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[8]/div/span')
#             # 验已还款额是否正确，是否为0；
#             yhke_money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[9]/div/span')
#             # 点击转账按钮；
#             self.driver.clic(self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
#             self.driver.clic(self.browser, 'xpath', '//*[@class="ivu-modal-content"]/div/div/div[3]/button[2]/span')
#             hkjg = self.driver.get_text(self.browser, 'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
#             time.sleep(7)
#             return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
#     except Exception, e:
#         logs.error_log(e)