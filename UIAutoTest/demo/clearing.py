# -*- coding: utf-8 -*-
from uitls.browser import browser
browser=browser()
from selenium.webdriver.common.by import By
from uitls import startend
from uitls import get_data
import sys,time,random

class aTestClearing(startend.PostlendTest):
        '''清贷测试'''
        def atest001(self):
                '''在贷客户发起清贷'''
                # 还款方式
                '''
                self.repayMethodText = u'等额本息'
                # 主借人姓名
                # self.customerName = unichr(random.randint(0x4e00, 0x9fa5)) + unichr(
                #         random.randint(0x4e00, 0x9fa5)) + unichr(random.randint(0x4e00, 0x9fa5))
                self.customerName ='周杰伦'
                # 贷款金额
                self.amount = int('30')
                # 认领金额
                self.claimmoney = '100'
                # 当前已还款金额
                self.alreadystillmoney = '0'
                # 还款信息条数
                self.nber = '0'
                # 所属部门
                # self.deptID = self.get_datas.config_json()[u'所属部门'][u'成都房贷一部']
                self.deptID = "33f1f497727b402c95607439f522ef68"
                # 资方主体
                # self.funder = self.get_datas.config_json()[u'资方主体'][u'外贸信托']
                # self.funderProductConfig = self.get_datas.config_json()[u'资方'][u'测试资方']
                self.funder ="0009800003"
                # 进件时间
                t1 = int(time.time())
                t2 = str(t1) + '000'
                time1 = int(t2)
                # 贷款产品
                # self.productId = self.get_datas.config_json()[u'贷款产品'][u'房贷一抵']
                # self.response = self.get_datas.get_datas(self.repayMethodText, self.customerName, self.deptID,
                #                                          self.funder,
                #                                          self.productId, self.amount, self.get_datas.get_code(),
                #                                          self.funderProductConfig, time1)
                self.productId = "0001000001"
                '''
                # 点击客户管理
                browser.click((By.ID,"tTopMenucustomer"))
                # 点击在贷客户
                browser.click((By.ID, "tSideMenuloanList"))
                # 根据主借人姓名查询
                browser.input((By.NAME,"tInputFilter"))
                browser.click((By.NAME,"tBtnFilter"))
                # 获取订单id
                #
                # self.ID = self.driver.get_text(self.browser, 'xpath', loan_clients.order_id_xpath)
                # # 点击订单编号，进入订单详情页；
                # self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")


# if __name__ == '__main__':
#     unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(test_test('testfirst002'))
#     suite.addTest(test_test('testfirst003'))
#     unittest.TextTestRunner().run(suite)