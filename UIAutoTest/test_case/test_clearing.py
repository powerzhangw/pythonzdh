#coding=utf-8
from uitls import startend
from selenium.webdriver.common.by import By
from uitls.post_result import *


class TestClearing(startend.PostlendTest):
#     '''详细信息-基本信息'''
    def test001(self):
        self.po = get_code()
        # 点击客户管理
        self.browser.click((By.ID, 'tTopMenucustomer'))
        # 点击在贷客户
        self.browser.click((By.XPATH, '//*[@id="tSideMenuloanList"]/span'))
        # 订单搜索
        self.browser.input((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input'),
                           '{0}'.format(self.po))
        self.browser.click((By.XPATH, '//*[text()=\"筛选\"]'))
        self.browser.wait(1)
        self.browser.click((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/button/span'))
        self.browser.click((By.XPATH, '/html/body/div[3]/ul/li[1]'))
        #发起清贷
        self.browser.click((By.XPATH,'//*[@class="ivu-icon ivu-icon-edit"]'))
        self.browser.wait(1)
        self.browser.click((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/table/tbody/tr/td[12]/div/div/div[2]/ul/li[3]/a'))
        self.browser.wait(1)

        #输入清贷日期 当天时间
        self.browser.click((By.XPATH,'//*[@placeholder="清贷时间"]'))
        self.browser.kenter((By.XPATH,'//*[@placeholder="清贷时间"]'))
        self.browser.click((By.XPATH,'//*[@name="tBtnLoanListClearingConfirm"]'))
        self.browser.wait(1)
        self.browser.scroll_top(5)
        # 确定提交
        self.browser.click((By.NAME, 'tBtnLoanListTrialModalConfirm'))
        self.browser.wait(2)
        # 点击清贷管理
        self.browser.click((By.XPATH,'//*[@id="tTopMenurepaymentRemoveLoan"]/span'))
        self.browser.click((By.ID,'tTopMenurepaymentRemoveLoan'))
        # 点击议定清贷
        self.browser.click((By.ID,'tSideMenuremoveLoan'))
        # 点击清贷列表
        self.browser.click((By.ID, 'tSideMenuremoveLoanremoveLoan-list'))
        self.browser.wait(1)
        # 搜索清贷客户
        self.browser.input((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input'),'{0}'.format(self.po))
        self.browser.kenter((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input'))
        self.browser.wait(2)
        # 提交审批
        self.browser.click((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[13]/div/div/a[1]'))
        self.browser.wait(2)
        # 点击清贷框
        self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[3]/div/div[1]/div[1]/div/span'))
        # 点击下拉框
        self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[3]/div/div/div[2]/ul[2]/li[2]'))
        # 输入议定清贷总额
        self.browser.input((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[7]/div/div[1]/input'),'244143')
        self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[7]/label'))
        self.browser.wait(2)
        self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[8]/div/div/span'))
        self.browser.input((By.XPATH,'/html/body/div[8]/div[2]/div/div/div[2]/div[1]/input'),'张巍巍')
        self.browser.wait(5)
        # 点击张巍巍，选中
        self.browser.kenter((By.XPATH,'/html/body/div[8]/div[2]/div/div/div[2]/div[1]/input'))
        self.browser.wait(1)
        # "/html/body/div[8]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div"
        self.browser.click((By.XPATH, '/html/body/div[8]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div'))
        self.browser.wait(1)
        # # 点击确定
        self.browser.click((By.XPATH, '/html/body/div[8]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div'))
        self.browser.wait(3)
        # 点击确定
        # 点击经理审批
        self.browser.click((By.XPATH, '//*[@id="tSideMenuremoveLoanremoveLoan-approval"]/span'))
        self.browser.input((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input'),'{0}'.format(self.po))
        self.browser.kenter((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input'))
        # 点击审批
        self.browser.click((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[14]/div/div/a'))
        # browser.input((By.NAME, "tInputFilter"))
        # browser.click((By.NAME, "tBtnFilter"))
        # print("断点断点断点断点断点断点")






