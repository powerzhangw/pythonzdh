#coding=utf-8
from common.payment_management import payment_deduction
from uitls import get_element
from uitls import log
from selenium.webdriver.common.keys import Keys
import sys,time
reload(sys)
sys.setdefaultencoding('utf8')
logs = log.log_message()

#公用关键字
#获取到翻页信息，截取当前有多少条数据，返回一个数字；
def page_date_num(str_number):
    number_data_01 = str_number[2:-2]
    number_data_02 = number_data_01.replace(' ','')
    return number_data_02

#千分位转换为数字；
def number_money(str_number):
    number_data_01 = str(str_number).replace(',','')
    money_number = float(number_data_01)
    return money_number

#贷前服务费应收金额
def ys_service_money(self,order_sn):
    # 点击服务费清单；
    self.driver.clic(self.browser,'xpath', '//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[4]')
    #将所有行的应收行金额进行相加；
    money01 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[1]/td[2]/div/span')
    money02 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[2]/td[2]/div/span')
    money03 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[3]/td[2]/div/span')
    money04 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[4]/td[2]/div/span')
    money05 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[5]/td[2]/div/span')
    money = float(money01) + float(money02) + float(money03) + float(money04) + float(money05)
    return money

#贷前服务费实收金额
def ss_service_money(self,order_sn):
    # 点击服务费清单；
    self.driver.clic(self.browser,'xpath','//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[4]')
    #将所有行的应收行金额进行相加；
    money01 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[1]/td[3]/div/span')
    money02 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[2]/td[3]/div/span')
    money03 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[3]/td[3]/div/span')
    money04 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[4]/td[3]/div/span')
    money05 = self.driver.get_text(self.browser,'xpath','//*[@name = "tTableBefore"]/div/div[2]/table/tbody/tr[5]/td[3]/div/span')
    money = float(money01) + float(money02) + float(money03) + float(money04) + float(money05)
    return money

#修改银行卡操作
def edit_bankcard(self,name):
    '''修改银行卡信息'''
    get_element.page_enter(self.browser,'客户卡管理')
    self.driver.element(self.browser,'name','tInputFilter').clear()
    self.driver.element(self.browser,'name','tInputFilter').send_keys(u'%s'%name)
    get_element.drow_down_input(self.browser,u'银行卡主要用途',u'还款')
    self.driver.clic(self.browser,'name','tBtnFilter')
    self.driver.clic(self.browser,'xpath','//*[@name="tTableCompany"]/div/div[2]/table/tbody/tr/td[16]/div/div/div[1]/i')
    self.driver.clic(self.browser,'xpath','//*[@name="tTableCompany"]/div/div[2]/table/tbody/tr/td[16]/div/div/div[2]/ul/li[1]')
    time.sleep(0.5)
    self.driver.drow_down_input(self.browser,u'银行卡账户类型',u'个人账户')
    time.sleep(0.5)
    self.driver.element(self.browser, 'xpath', '//*[@name="tInputmaster"]/div/div[1]/input').clear()
    self.driver.element(self.browser, 'xpath', '//*[@name="tInputmaster"]/div/div[1]/input').send_keys(u'%s'%name)
    self.driver.drow_down_input(self.browser, u'银行卡证件类型', u'身份证')
    self.driver.element(self.browser, 'xpath', '//*[@name="tInputidentNo"]/div/div[1]/input').clear()
    self.driver.element(self.browser, 'xpath', '//*[@name="tInputidentNo"]/div/div[1]/input').send_keys('510521198612140711')
    self.driver.drow_down_input(self.browser, u'银行卡分支行', u'默认')
    self.driver.clic(self.browser,'name','tBtnConfirmEditBank')
    self.text = self.driver.get_text(self.browser, 'xpath','/html/body/div[9]/div/div[1]/div/div[2]')
    return self.text

#划扣操作
def deduction_money(self,ID,claim_money,zifang,hklx=None,czuo=u'划扣'):
    try:
        #关闭所有标签
        get_element.close_all_tab(self.browser,text='all')
        # 进入划扣列表
        get_element.page_enter(self.browser, u'待还列表')
        if zifang == u'易捷' and hklx == u'正常待还' and czuo == u'划扣':
            # 进入划扣页面-点击待还列表按钮
            self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
            # 进入划扣页面-点击易捷按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
            # 进入划扣页面-点击正常待还按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_normalrepaymentpath)
            # 根据id查询出订单
            self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).clear()
            self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).send_keys('%s'%ID)
            self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_confirmname)
            # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
            # 验证应还总额是否正确，等于贷前费用；
            yhze_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yh_money)
            # 验证预还款额是否正确,是否为0；
            yhkje_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_money)
            # 验已还款额是否正确，是否为0；
            yhke_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_hk_money)
            check_elements(self,self.browser,'xpath', payment_deduction.wait_repayment_hk_money)
            # 点击划扣按钮,输入划扣金额；
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_deductionpath)
            # self.logs.info_log(u'还款管理页面，进入划扣页面，划扣金额，验证划扣是否成功；')
            check_elements(self, self.browser, 'xpath', payment_deduction.wait_repayment_yhk_xpath)
            self.driver.element(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_xpath).clear()
            self.driver.element(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_xpath).send_keys('%s'%claim_money)
            # 选择划扣时间为当前日期；
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_hksj_xpath)
            self.driver.element(self.browser, 'xpath', payment_deduction.wait_repayment_hksj_xpath).send_keys(Keys.ENTER)
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_hksj_button_xpath)
            # 账户选择下拉框，选择对应的账户；
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zhhm_xpath)
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zhhm_xpath_01)
            # 划扣确认页面，点击确定按钮,验证提示“划扣成功”
            self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_submit_name)
            hkjg = self.driver.get_text(self.browser,'xpath', '//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            time.sleep(7)
            return {u'应还总额':yhze_money,u'预划扣额':yhkje_money,u'已还款额':yhke_money,u'划扣结果':hkjg}
        elif zifang == u'易捷' and hklx == u'逾期待还'and czuo == u'划扣':
            # 进入划扣页面-点击待还列表按钮
            self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
            # 进入划扣页面-点击易捷按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
            # 进入划扣页面-点击逾期待还按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_overduerepaymentpath)
            # 根据id查询出订单
            self.driver.element(self.browser, 'xpath',
                                '//div[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//div[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'%ID)
            self.driver.clic(self.browser, 'xpath', '//div[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[1]/form/div[6]/div/button[1]/span')
            # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
            # 验证应还总额是否正确，等于贷前费用；
            yhze_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[7]/div/span')
            # 验证预还款额是否正确,是否为0；
            yhkje_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div/span')
            # 验已还款额是否正确，是否为0；
            yhke_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/span')
            check_elements(self,self.browser,'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/span')
            # 点击划扣按钮,输入划扣金额；
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductWaitEJ"]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[1]')
            # self.logs.info_log(u'还款管理页面，进入划扣页面，划扣金额，验证划扣是否成功；')
            self.driver.element(self.browser, 'xpath','/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath','/html/body/div[8]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys('%s'%claim_money)
            # 选择划扣时间为当前日期；
            self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input')
            self.driver.element(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
            self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/div/div/div/div[4]/button[3]/span')
            # 账户选择下拉框，选择对应的账户；
            self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/div[1]/div/span')
            self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li')
            check_elements(self, self.browser, 'xpath','/html/body/div[8]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li')
            # 划扣确认页面，点击确定按钮,验证提示“划扣成功”
            self.driver.clic(self.browser, 'xpath', '/html/body/div[8]/div[2]/div/div/div[3]/div/button[2]')
            hkjg = self.driver.get_text(self.browser, 'xpath', '//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            time.sleep(7)
            return {u'应还总额':yhze_money,u'预划扣额':yhkje_money,u'已还款额':yhke_money,u'划扣结果':hkjg}
        elif zifang == u'资方' and hklx == None and czuo == u'划扣':
            # 进入划扣页面-点击待还列表按钮
            self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
            # 进入划扣页面-点击资方按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zfpath)
            # 根据id查询出订单
            self.driver.element(self.browser, 'xpath',
                                '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'%ID)
            self.driver.clic(self.browser, 'xpath', '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/form/div[6]/div/button[1]')
            # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
            # 验证应还总额是否正确，等于贷前费用；
            yhze_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[7]/div/span')
            # 验证预还款额是否正确,是否为0；
            yhkje_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[8]/div/span')
            # 验已还款额是否正确，是否为0；
            yhke_money = self.driver.get_text(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[9]/div/span')
            check_elements(self,self.browser,'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[9]/div/span')
            # 点击划扣按钮,输入划扣金额；
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[10]/div/div/a[1]')
            # self.logs.info_log(u'还款管理页面，进入划扣页面，划扣金额，验证划扣是否成功；')
            self.driver.element(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[3]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys('%s'%claim_money)
            # 选择划扣时间为当前日期；
            self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input')
            self.driver.element(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/input').send_keys(
                Keys.ENTER)
            self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/div/div/div/div[4]/button[3]/span')
            # 账户选择下拉框，选择对应的账户；
            self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[5]/div/div/div[1]/div/span')
            self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li')
            check_elements(self, self.browser, 'xpath','/html/body/div[9]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li')
            # 划扣确认页面，点击确定按钮,验证提示“划扣成功”
            self.driver.clic(self.browser, 'xpath', '/html/body/div[9]/div[2]/div/div/div[3]/div/button[2]/span')
            hkjg = self.driver.get_text(self.browser, 'xpath', '//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            time.sleep(7)
            return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
        elif zifang == u'易捷' and hklx == u'正常待还' and czuo == u'转账':
            # 进入划扣页面-点击待还列表按钮
            self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
            # 进入划扣页面-点击易捷按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
            # 进入划扣页面-点击正常待还按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_normalrepaymentpath)
            # 根据id查询出订单
            self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).clear()
            self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).send_keys('%s'%ID)
            self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_confirmname)
            # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
            # 验证应还总额是否正确，等于贷前费用；
            yhze_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yh_money)
            # 验证预还款额是否正确,是否为0；
            yhkje_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_money)
            # 验已还款额是否正确，是否为0；
            yhke_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_hk_money)
            # 点击转账按钮，进入转账页面；
            self.driver.clic(self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
            check_elements(self, self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
            self.driver.clic(self.browser,'xpath','//*[@class="ivu-modal-content"]/div/div/div[3]/button[2]/span')
            hkjg = self.driver.get_text(self.browser, 'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            time.sleep(7)
            return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
        elif zifang == u'易捷' and hklx == u'逾期待还' and czuo == u'转账':
            # 进入划扣页面-点击待还列表按钮
            self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
            # 进入划扣页面-点击易捷按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_ejiepath)
            # 进入划扣页面-点击正常待还按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_normalrepaymentpath)
            # 根据id查询出订单
            self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).clear()
            self.driver.element(self.browser, 'name', payment_deduction.wait_repayment_ordername).send_keys('%s'%ID)
            self.driver.clic(self.browser, 'name', payment_deduction.wait_repayment_confirmname)
            # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
            # 验证应还总额是否正确，等于贷前费用；
            yhze_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yh_money)
            # 验证预还款额是否正确,是否为0；
            yhkje_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_yhk_money)
            # 验已还款额是否正确，是否为0；
            yhke_money = self.driver.get_text(self.browser, 'xpath', payment_deduction.wait_repayment_hk_money)
            # 点击转账按钮，进入转账页面；
            self.driver.clic(self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
            check_elements(self, self.browser, 'xpath','//*[@class="ivu-tabs-content"]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
            self.driver.clic(self.browser,'xpath','//*[@class="ivu-modal-content"]/div/div/div[3]/button[2]/span')
            hkjg = self.driver.get_text(self.browser, 'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            time.sleep(7)
            return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
        elif zifang == u'资方' and hklx == None and czuo == u'转账':
            # 进入划扣页面-点击待还列表按钮
            self.driver.clic(self.browser, 'id', payment_deduction.wait_repayment_listid)
            # 进入划扣页面-点击资方按钮
            self.driver.clic(self.browser, 'xpath', payment_deduction.wait_repayment_zfpath)
            # 根据id查询出订单
            self.driver.element(self.browser, 'xpath',
                                '//*[@name="tTagDeductWait"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@name="tTagDeductWait"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'%ID)
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductWait"]/div[2]/div[2]/div/div[1]/form/div[6]/div/button[1]')
            # 获取应还总额，预划扣额，已还款额判断是否正确（应还总额，应该等于全部贷前费用，预划扣额应该为0，已还款额应该为0）；
            # 验证应还总额是否正确，等于贷前费用；
            yhze_money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[7]/div/span')
            # 验证预还款额是否正确,是否为0；
            yhkje_money = self.driver.get_text(self.browser, 'xpath',
                                               '//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[8]/div/span')
            # 验已还款额是否正确，是否为0；
            yhke_money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[9]/div/span')
            # 点击转账按钮；
            self.driver.clic(self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
            check_elements(self, self.browser, 'xpath','//*[@name="tTableDeductWaitFunder"]/div/div[2]/table/tbody/tr/td[10]/div/div/a[2]')
            self.driver.clic(self.browser, 'xpath', '//*[@class="ivu-modal-content"]/div/div/div[3]/button[2]/span')
            hkjg = self.driver.get_text(self.browser, 'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            time.sleep(7)
            return {u'应还总额': yhze_money, u'预划扣额': yhkje_money, u'已还款额': yhke_money, u'划扣结果': hkjg}
    except Exception, e:
        logs.error_log(e)

#划扣列表记录
def deduction_recordlist(self ,ID ,text=u'易捷' ,hklx=u'正常待还'):
    try:
        # 先关闭所有标签，然后再进行操作
        get_element.close_all_tab(self.browser, text='all')
        get_element.page_enter(self.browser, u'划扣列表')
        if text == u'易捷' and hklx == u'正常待还':
            self.driver.clic(self.browser ,'xpath' ,'//*[@name="tTagDeductList"]/div[1]/div/div/div/div/div[2]')
            self.driver.clic(self.browser ,'xpath' ,'//*[@name="tTagDeductListEJ"]/div[1]/div/div/div/div/div[2]')
            self.driver.element(self.browser, 'xpath','//*[@name="tTagDeductListEJ"]/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@name="tTagDeductListEJ"]/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input').send_keys('%s' %ID)
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductListEJ"]/div[2]/div[1]/div/div[1]/form/div[8]/div/button[1]')
            yeshu = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductListEJ"]/div[2]/div[1]/div/div[4]/ul/span')
            if page_date_num(yeshu) != '0' :
                money = self.driver.get_text(self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[3]/div/div[2]/table/tbody/tr/td[8]/div/span')
                status = self.driver.get_text(self.browser, 'xpath', '//*[@class="ivu-tabs-content"]/div[1]/div/div[3]/div/div[2]/table/tbody/tr/td[10]/div/span')
                return {u"预划扣金额" :money ,u"预划扣状态" :status}
            else:
                aaa= u'订单不存在'
                return aaa
        elif text == u'易捷' and hklx == u'逾期待还':
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductList"]/div[1]/div/div/div/div/div[2]')
            self.driver.clic(self.browser ,'xpath' ,'//*[@name="tTagDeductListEJ"]/div[1]/div/div/div/div/div[3]')
            self.driver.element(self.browser, 'xpath','//*[@name="tTagDeductListEJ"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@name="tTagDeductListEJ"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s' % ID)
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductListEJ"]/div[2]/div[2]/div/div[1]/form/div[8]/div/button[1]')
            yeshu = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductListEJ"]/div[2]/div[2]/div/div[4]/ul/span')
            if page_date_num(yeshu) != '0':
                money = self.driver.get_text(self.browser, 'xpath','//*[@active="tTagDeductListEJOverdue"]/div[3]/div/div[2]/table/tbody/tr/td[8]/div/span')
                status = self.driver.get_text(self.browser, 'xpath','//*[@active="tTagDeductListEJOverdue"]/div[3]/div/div[2]/table/tbody/tr/td[10]/div/span')
                return {u"预划扣金额": money, u"预划扣状态": status}
            else:
                aaa = u'订单不存在'
                return aaa
        elif text == u'资方' and hklx == None:
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductList"]/div[1]/div/div/div/div/div[3]')
            self.driver.element(self.browser, 'xpath','//*[@name="tTagDeductList"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@name="tTagDeductList"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s'% ID)
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductList"]/div[2]/div[2]/div/div[1]/form/div[8]/div/button[1]')
            yeshu = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductList"]/div[2]/div[2]/div/div[4]/ul/span')
            if page_date_num(yeshu) != '0':
                money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductListFunder"]/div/div[2]/table/tbody/tr[1]/td[8]/div/span')
                status = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductListFunder"]/div/div[2]/table/tbody/tr[1]/td[10]/div/span')
                return {u"预划扣金额": money, u"预划扣状态": status}
            else:
                aaa = u'订单不存在'
                return aaa
    except Exception, e:
        logs.error_log(e)

#划扣历史
def deduction_recordhistroy(self ,ID ,text = u'易捷' ,hklx=u'正常待还'):
    try:
        # 先关闭所有标签，然后再进行操作
        get_element.close_all_tab(self.browser, text='all')
        get_element.page_enter(self.browser, u'历史划扣')
        if text == u'易捷' and hklx == u'正常待还':
            self.driver.element(self.browser, 'xpath','//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input').send_keys('%s' %self.ID)
            self.driver.clic(self.browser, 'xpath', '//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[1]/form/div[8]/div/button[1]')
            yeshu = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[3]/ul/span')
            if page_date_num(yeshu) != '0':
                money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/div/span')
                money01 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/div/span')
                status = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/span')
                return {u"预划扣金额": money ,u"实际扣款额": money01, u"预划扣状态": status}
            else:
                text = u'订单不存在'
                return text
        elif text == u'易捷' and hklx == u'逾期待还':
            self.driver.clic(self.browser ,'xpath' ,'//*[@name="tTagDeductHistoryEJ"]/div[1]/div/div/div/div/div[3]')
            self.driver.element(self.browser, 'xpath','//*[@active="tTagDeductHistoryEJOverdue"]/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath', '//*[@active="tTagDeductHistoryEJOverdue"]/div[1]/form/div[1]/div/div/input').send_keys('%s' %self.ID)
            self.driver.clic(self.browser, 'xpath', '//*[@active="tTagDeductHistoryEJOverdue"]/div[1]/form/div[8]/div/button[1]')
            yeshu = self.driver.get_text(self.browser, 'xpath','//*[@active="tTagDeductHistoryEJOverdue"]/div[3]/ul/span')
            if page_date_num(yeshu) != '0':
                money = self.driver.get_text(self.browser, 'xpath','//*[@active="tTagDeductHistoryEJOverdue"]/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/div/span')
                money01 = self.driver.get_text(self.browser, 'xpath','//*[@active="tTagDeductHistoryEJOverdue"]/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/div/span')
                status = self.driver.get_text(self.browser, 'xpath','//*[@active="tTagDeductHistoryEJOverdue"]/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div/span')
                return {u"预划扣金额": money ,u"实际扣款额": money01, u"预划扣状态": status}
            else:
                text = u'订单不存在'
                return text
        elif text == u'资方' and  hklx == None:
            self.driver.clic(self.browser ,'xpath' ,'//*[@name="tTagDeductHistory"]/div[1]/div/div/div/div/div[3]')
            self.driver.element(self.browser ,'xpath','//*[@name="tTagDeductHistory"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.element(self.browser, 'xpath','//*[@name="tTagDeductHistory"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input').send_keys('%s' %self.ID)
            self.driver.clic(self.browser ,'xpath','//*[@name="tTagDeductHistory"]/div[2]/div[2]/div/div[1]/form/div[8]/div/button[1]')
            yeshu = self.driver.get_text(self.browser, 'xpath','//*[@name="tTagDeductHistory"]/div[2]/div[2]/div/div[3]/ul/span')
            if page_date_num(yeshu) != '0':
                money = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductHistoryFunder"]/div/div[2]/table/tbody/tr[1]/td[7]/div/span')
                money01 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductHistoryFunder"]/div/div[2]/table/tbody/tr[1]/td[8]/div/span')
                status = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableDeductHistoryFunder"]/div/div[2]/table/tbody/tr[1]/td[10]/div/span')
                return {u"预划扣金额": money ,u"实际扣款额": money01, u"预划扣状态": status}
            else:
                text = u'订单不存在'
                return text
    except Exception, e:
        logs.error_log(e)

#清贷
def clearing_loan(self,ID):
    try:
        #点击清贷按钮，进入清贷页面
        get_element.close_all_tab(self.browser, text='all')
        get_element.page_enter(self.browser, u'在贷客户')
        self.driver.element(self.browser,'xpath','//*[@name="tInputFilter"]').clear()
        self.driver.element(self.browser,'xpath','//*[@name="tInputFilter"]').send_keys('%s'%ID)
        self.driver.clic(self.browser,'xpath','//*[@name="tBtnFilter"]')
        self.driver.clic(self.browser,'xpath','//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr/td[12]/div/div/div[1]/i')
        self.driver.clic(self.browser,'xpath','//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr/td[12]/div/div/div[2]/ul/li[3]/a')
        self.driver.clic(self.browser,'xpath','//*[@placeholder="清贷时间"]')
        self.driver.element(self.browser,'xpath','//*[@placeholder="清贷时间"]').send_keys(Keys.ENTER)
        self.driver.clic(self.browser,'xpath','//*[@name="tBtnLoanListClearingConfirm"]')
        txt = self.driver.get_text(self.browser,'xpath','//*[@name="tTableBaseInfo"]/../../../div[1]')
        if txt == u'试算结果预览':
            logs.info_log("进入试算预览页面")
            self.jiekuanren = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableBaseInfo"]/tbody/tr[2]/td[1]')  # 借款人
            self.jiekuanjine = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableBaseInfo"]/tbody/tr[2]/td[2]')  # 借款金额
            self.dangqianqici = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableBaseInfo"]/tbody/tr[2]/td[7]')  # 当前期次
            self.qingdaibenjin = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[2]/td[3]')  # 清贷本金
            self.qindailixi = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[3]/td[2]')  # 清贷利息
            self.zifangfuwufei = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[4]/td[2]')  # 资方服务费
            self.daishoudaibanfwf = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[5]/td[3]')  # 代收代付经纪人服务费
            self.daishoudaifudsf = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[6]/td[2]')  # 代收代付第三方服务费
            self.daibanfuwufei = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[7]/td[3]')  # 代办服务费
            self.t_001 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[8]/td[2]')  # 信息服务费-次收1
            self.t_002 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[9]/td[2]')  # 信息服务费-次收2
            self.t_003 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[10]/td[2]')  # 信息服务费-期收
            self.t_004 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[11]/td[2]')  # 信息服务费-逾还
            self.t_005 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[12]/td[2]')  # 信息服务费-提还
            self.t_006 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[13]/td[2]')  # 合计应收服务费
            self.t_007 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[14]/td[2]')  # 服务费折让1
            self.t_008 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[15]/td[2]')  # 服务费折让2
            self.t_009 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[16]/td[2]')  # 服务费折让3
            self.t_0010 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[17]/td[2]')  # 服务费折让4
            self.t_0011 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[18]/td[2]')  # 合计服务费折让
            self.t_0012 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[19]/td[2]')  # 应收清贷总额
            self.t_0013 = self.driver.get_text(self.browser, 'xpath','//*[@name="tTableClearInfo"]/tbody/tr[20]/td[2]')  # 还款余额
            self.driver.clic(self.browser,'xpath','//*[@name="tBtnLoanListTrialModalConfirm"]')
            text = self.driver.get_text(self.browser,'xpath','//*[@class="ivu-notice"]/div/div[1]/div/div[2]')
            dict = {u"借款人": "%s" % self.jiekuanren, u"借款金额": "%s" % self.jiekuanjine, u"当前期次": "%s" % self.dangqianqici,
                    u"清贷本金": "%s" % self.qingdaibenjin, u"清贷利息": "%s" % self.qindailixi,
                    u"资方服务费": "%s" % self.zifangfuwufei, u"代收代付经纪人服务费": "%s" % self.daishoudaifudsf,
                    u"代收代付第三方服务费": "%s" % self.daishoudaifudsf, u"代办服务费": "%s" % self.daibanfuwufei,
                    u"信息服务费-次收1": "%s" % self.t_001, u"信息服务费-次收2": "%s" % self.t_002, u"信息服务费-期收": "%s" % self.t_003,
                    u"信息服务费-逾还": "%s" % self.t_004, u"信息服务费-提还": "%s" % self.t_005, u"合计应收服务费": "%s" % self.t_006,
                    u"服务费折让1": "%s" % self.t_007, u"服务费折让2": "%s" % self.t_008, u"服务费折让3": "%s" % self.t_009,
                    u"服务费折让4": "%s" % self.t_0010, u"合计服务费折让": "%s" % self.t_0011, u"应收清贷总额": "%s" % self.t_0012,
                    u"还款余额": "%s" % self.t_0013,u'试算结果':"%s"%text}
            return dict
        else:
            logs.error_log("进入试算预览失败")
    except Exception,e:
        logs.error_log(e)

#进行对比，输入对比参数，若失败截图
def assert_result(self,result01,result02,text_result=u'测试结果'):
    if result01 == result02:
        self.logs.info_log(u'%s'%text_result)
    else:
        get_element.get_screen(self.browser)
        self.assertEqual(result01,result02)

#查找页面元素，若失败截图
def check_elements(self,driver,method,location):
    logs.info_log(u'获取定位' + method + ':' + location)
    time.sleep(0.5)
    try:
        if method == 'id':
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_id(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素id不存在，截图保存;%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        elif method == "name":
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_name(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素不存在，截图保存,%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        elif method == "class":
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_class_name(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素不存在，截图保存,%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        elif method == "link_text":
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_link_text(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素不存在，截图保存,%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        elif method == "xpath":
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_xpath(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素不存在，截图保存,%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        elif method == "tag":
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_tag_name(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素不存在，截图保存,%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        elif method == "css":
            get_element.element_wait(driver, method, location)
            element = driver.find_elements_by_css_selector(location)
            if len(element) == 1:
                pass
            elif len(element) == 0:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素不存在，截图保存,%s;'%location)
                self.assertEqual(True,False)
            else:
                get_element.get_screen(self.browser)
                self.logs.error_log(u'元素存在%s个，截图,%s'%(len(element),location))
                self.assertEqual(True,False)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element
    except Exception, e:
        logs.error_log(e)