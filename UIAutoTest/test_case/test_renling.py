# -*- coding: utf-8 -*-
#coding=utf-8
from uitls import startend
from selenium.webdriver.common.by import By
from uitls.post_result import *


class TestRenling(startend.PostlendTest):
#     '''详细信息-基本信息'''
    def test_rl(self):

        self.po = get_code()
        # 点击客户管理
        self.browser.click((By.ID, 'tTopMenucustomer'))
        # 点击在贷客户
        self.browser.click((By.XPATH, '//*[@id="tSideMenuloanList"]/span'))
        # 订单搜索
        self.browser.input((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/input'),
                           '{0}'.format(self.po))
        self.browser.click((By.XPATH, '//*[text()=\"筛选\"]'))
        # 点击订单编号，进入订单详情页；
        self.browser.wait(2)
        self.browser.click((By.XPATH,"//*[text()= '{0}']".format(self.po)))
        # 验证订单各数据是否正确；
        self.log.info(u'获取订单相关信息，验证金额、客户名、当前贷款期限、当前还款信息等是否正确')
        # 验证客户姓名是否正确
        self.po = randomname()
        log.info("这是进件时的name:{0}".format(self.po))
        self.getname = self.browser.get_text((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]'))
        log.info("这是前段获取到的name:{0}".format(self.getname))
        self.assertNotEqual (self.po,self.getname)
        是是是

        # self.customer_name = self.driver.get_text(self.browser, 'xpath', order_detail.customer_name)
    #     public_keyword.assert_result(self,self.customerName, self.customer_name,text_result=u'客户姓名与进件时客户姓名相同，正确；')
    #     # self.assertEqual(self.customerName, self.customer_name)
        # 验证贷款金额是否正确
    #     self.customer_amount = self.driver.get_text(self.browser, 'xpath', order_detail.customer_amount)
    #     public_keyword.assert_result(self, public_keyword.number_money(self.customer_amount), float(self.amount * 10000), text_result=u'贷款金额与进件时金额相同，正确；')
    #     # self.assertEqual(public_keyword.number_money(self.customer_amount), float(self.amount * 10000))
    #     # 验证当前还款期限是否为第一期
    #     self.customer_repaid_now = self.driver.get_text(self.browser, 'xpath', order_detail.customer_already_repaid)
    #     # 点击还款信息,验证当前还款信息是否正确
    #     self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
    #     self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
    #     public_keyword.assert_result(self,public_keyword.page_date_num(self.page), self.nber,text_result=u'还款信息页面，还款记录为0，正确；')
    #     # self.assertEqual(public_keyword.page_date_num(self.page), self.nber)
    #     # 查询贷前费用实收总和；
    #     self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
    #     # 查询贷前费用应收总和；
    #     self.dqfy_yinshou = public_keyword.ys_service_money(self, self.ID)
    #     self.logs.info_log(u'3、还款管理页面，进入认领页面，进行认领等操作；')
    #     # 进入认领页面-点击还款管理，认领管理按钮
    #     self.driver.clic(self.browser, 'id', payment_deduction.repayment_button_id)
    #     self.driver.clic(self.browser, 'id', payment_claim.claim_management_id)
    #     # 进入认领页面-点击认领列表按钮
    #     self.driver.clic(self.browser, 'id', payment_claim.claim_management_list_id)
    #     # 进入认领页面-点击易捷按钮
    #     self.driver.clic(self.browser, 'xpath', payment_claim.claim_management_list_yj_xpath)
    #     # 进入认领页面-根据户名查找回盘流水；
    #     self.driver.element(self.browser, 'name', payment_claim.claim_management_list_zf_namequery_name).clear()
    #     self.driver.element(self.browser,'name', payment_claim.claim_management_list_zf_namequery_name).send_keys(u'自动化测试')
    #     self.driver.clic(self.browser, 'name', payment_claim.claim_management_list_zf_submit_name)
    #     # 进入认领页面-点击认领按钮
    #     self.driver.clic(self.browser, 'xpath', payment_claim.claim_management_list_yj_snclaim_xpath)
    #     # 输入认领金额1000元；
    #     self.driver.element(self.browser,'xpath', payment_claim.claim_management_list_yj_claimmoney_xpath).clear()
    #     self.driver.element(self.browser,'xpath', payment_claim.claim_management_list_yj_claimmoney_xpath).send_keys('%s'%self.claimmoney)
    #     #认领类型选择“正常”,并点击确定按钮；
    #     get_element.drow_down_input(self.browser,u'认领类型',u'正常')
    #     self.driver.clic(self.browser,'name',payment_claim.claim_management_list_yj_submit_name)
    #     #选择选择对应的输入框，查询需要认领的订单,验证查询出的数据是否只有一条；
    #     self.driver.element(self.browser,'name',payment_claim.claim_management_sn_name).clear()
    #     self.driver.element(self.browser, 'name', payment_claim.claim_management_sn_name).send_keys('%s'%self.ID)
    #     self.driver.clic(self.browser,'name',payment_claim.claim_management_sn_submit_name)
    #     self.page = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_datelist_xpath)
    #     self.assertEqual(public_keyword.page_date_num(self.page), "1")
    #     self.driver.clic(self.browser,'xpath',payment_claim.claim_management_submitclaim_xpath)
    #     #在认领确认页面，验证认领金额，认领类型，档案编号和借款人姓名是否正确；
    #     self.money = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_money)
    #     self.type = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_type)
    #     self.sn = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_snno)
    #     self.name = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_borrowername)
    #     self.assertEqual(public_keyword.number_money(self.claimmoney),public_keyword.number_money(self.money))
    #     self.assertEqual(self.type,u'正常')
    #     self.assertEqual(self.name,self.customerName)
    #     #认领确认页面，点击确定按钮,验证提示“确认认领成功”
    #     self.driver.clic(self.browser,'name',payment_claim.claim_management_submitclaimcheck_submitname)
    #     self.text = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_promptbox)
    #     self.assertEqual(self.text, u'确认认领成功')
    #     self.logs.info_log(u'4、认领成功后，检查历史认领，各数据是否正确；')
    #     #检查历史认领记录，是否正常；
    #     get_element.page_enter(self.browser,u'历史认领')
    #     self.driver.element(self.browser, 'name', clients_list.number_input_name).clear()
    #     self.driver.element(self.browser,'name',clients_list.number_input_name).send_keys(self.ID)
    #     time.sleep(1)
    #     self.driver.clic(self.browser,'css',loan_clients.Filter_clic_css)
    #     #历史认领中，该订单存在一张认领记录，且金额和认领类型正确
    #     self.page = self.driver.get_text(self.browser,'xpath',payment_claim.claim_management_histroydatas_xpath)
    #     self.assertEqual(public_keyword.page_date_num(self.page), "1")
    #     self.money_01 = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_histroydatasmoney_xpath)
    #     self.assertEqual(public_keyword.number_money(self.money_01),public_keyword.number_money(self.claimmoney))
    #     self.type_01 = self.driver.get_text(self.browser, 'xpath',payment_claim.claim_management_histroydatastype_xpath)
    #     self.assertEqual(self.type_01, u'正常')
    #     #点击查看按钮，进入历史认领详情页，验证各数据是否正确；
    #     self.driver.clic(self.browser,'xpath',payment_claim.claim_management_histroydatastype_button)
    #     self.money_02 = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_histroydatasmoney_xpath01)
    #     self.assertEqual(public_keyword.number_money(self.money_01), public_keyword.number_money(self.claimmoney))
    #     self.type_02 = self.driver.get_text(self.browser, 'xpath',payment_claim.claim_management_histroydatastype_xpath01)
    #     self.assertEqual(self.type_02, u'正常')
    #     self.ID_02 = self.driver.get_text(self.browser, 'xpath',payment_claim.claim_management_histroydatasID_xpath01)
    #     self.assertEqual(self.ID_02, self.ID)
    #     #进入订单详情页，验证认领数据是否正确；
    #     self.logs.info_log(u'5、进入订单详情页，检查还款信息以及服务费清单数据是否正确；')
    #     self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")
    #     self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
    #     self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
    #     self.assertEqual(public_keyword.page_date_num(self.page), "1")
    #     self.text01 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_way_xpath)
    #     self.assertIn(u'认领',self.text01)
    #     self.text02 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_money_xpath)
    #     self.assertEqual(public_keyword.number_money(self.text02), public_keyword.number_money(self.claimmoney))
    #     #进入订单详情页，验证服务费清单实收金额是否等于认领金额；
    #     self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
    #     self.assertEqual(public_keyword.number_money(self.dqfy_shishou),public_keyword.number_money(self.claimmoney))
    #
    # def test_02_claim_index(self):
    #     '''验证新进订单，进行贷前和第一期期还认领操作'''
    #     self.logs.info_log(u'验证新进订单，进行贷前和第一期期还认领操作；')
    #     self.logs.info_log(u'1、使用接口进单；')
    #     # 还款方式
    #     self.repayMethodText = u'等额本息'
    #     # 主借人姓名
    #     self.customerName = unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5))
    #     # 贷款金额
    #     self.amount = int('30')
    #     # 当前已还款金额
    #     self.alreadystillmoney = '0'
    #     # 还款信息条数
    #     self.nber = '0'
    #     # 所属部门
    #     self.deptID = self.get_datas.config_json()[u'所属部门'][u'成都房贷一部']
    #     # 资方主体
    #     self.funder = self.get_datas.config_json()[u'资方主体'][u'外贸信托']
    #     self.funderProductConfig = self.get_datas.config_json()[u'资方'][u'测试资方']
    #     # 进件时间
    #     t1 = int(time.time()) - int(2419200)
    #     t2 = str(t1) + '000'
    #     time1 = int(t2)
    #     # 贷款产品
    #     self.productId = self.get_datas.config_json()[u'贷款产品'][u'房贷一抵']
    #     self.response = self.get_datas.get_datas(self.repayMethodText, self.customerName, self.deptID, self.funder,
    #                                            self.productId, self.amount,self.get_datas.get_code(),self.funderProductConfig,time1)
    #     self.assertEqual(self.response,u'成功')
    #     # 点击客户管理
    #     self.driver.clic(self.browser, 'xpath', loan_clients.clients_management_clic_xpath)
    #     # 点击在贷客户
    #     self.driver.clic(self.browser, 'xpath', loan_clients.loan_clients_clic_xpath)
    #     # 根据主借人姓名查询
    #     time.sleep(1.5)
    #     self.driver.element(self.browser, 'name', loan_clients.number_input_name).clear()
    #     self.driver.element(self.browser, 'name', loan_clients.number_input_name).send_keys('%s'%self.customerName)
    #     # 获取订单id,并跑批
    #     self.ID = self.driver.get_text(self.browser, 'xpath', loan_clients.order_id_xpath)
    #     self.response = get_data.batch_task('%s'%self.ID)
    #     self.assertEqual(self.response, u'成功')
    #     # 点击订单编号，进入订单详情页；
    #     self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")
    #     # 验证订单各数据是否正确；
    #     self.logs.info_log(u'2、获取订单相关信息，验证金额、客户名、当前贷款期限、当前还款信息等是否正确；')
    #     # 验证客户姓名是否正确
    #     self.customer_name = self.driver.get_text(self.browser, 'xpath', order_detail.customer_name)
    #     public_keyword.assert_result(self,self.customerName, self.customer_name,text_result=u'用户名和进单用户名一致，正确；')
    #     # self.assertEqual(self.customerName, self.customer_name)
    #     # 验证贷款金额是否正确
    #     self.customer_amount = self.driver.get_text(self.browser, 'xpath', order_detail.customer_amount)
    #     self.assertEqual(public_keyword.number_money(self.customer_amount), float(self.amount * 10000))
    #     # 验证当前还款期限是否为第一期
    #     self.customer_repaid_now = self.driver.get_text(self.browser, 'xpath', order_detail.customer_already_repaid)
    #     # 点击还款信息,验证当前还款信息是否正确
    #     self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
    #     self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
    #     public_keyword.assert_result(self,public_keyword.page_date_num(self.page), self.nber,text_result=u'还款记录表，还款记录为0，正确；')
    #     # self.assertEqual(public_keyword.page_date_num(self.page), self.nber)
    #     # 查询贷前费用实收总和；
    #     self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
    #     # 查询贷前费用应收总和；
    #     self.dqfy_yinshou = public_keyword.ys_service_money(self, self.ID)
    #     # 查询借款人表第一期期还的金额以及；
    #     dict_01 = get_element.get_payment_datas(self.browser,u'易捷表')
    #     self.qihuan_money = dict_01[u'第1期-本期合计应收款额']
    #     self.logs.info_log(u'3、还款管理页面，进入认领页面，进行认领等操作；')
    #     # 进入认领页面-点击还款管理，认领管理按钮
    #     self.driver.clic(self.browser, 'id', payment_deduction.repayment_button_id)
    #     self.driver.clic(self.browser, 'id', payment_claim.claim_management_id)
    #     # 进入认领页面-点击认领列表按钮
    #     self.driver.clic(self.browser, 'id', payment_claim.claim_management_list_id)
    #     # 进入认领页面-点击易捷按钮
    #     self.driver.clic(self.browser, 'xpath', payment_claim.claim_management_list_yj_xpath)
    #     # 进入认领页面-根据户名查找回盘流水；
    #     self.driver.element(self.browser, 'name', payment_claim.claim_management_list_zf_namequery_name).clear()
    #     self.driver.element(self.browser,'name', payment_claim.claim_management_list_zf_namequery_name).send_keys(u'自动化测试')
    #     self.driver.clic(self.browser, 'name', payment_claim.claim_management_list_zf_submit_name)
    #     # 进入认领页面-点击认领按钮
    #     self.driver.clic(self.browser, 'xpath', payment_claim.claim_management_list_yj_snclaim_xpath)
    #     # 输入认领金额为期还和贷前费用总和；
    #     self.money_all = public_keyword.number_money(self.qihuan_money) + public_keyword.number_money(self.dqfy_yinshou)
    #     self.driver.element(self.browser,'xpath', payment_claim.claim_management_list_yj_claimmoney_xpath).clear()
    #     self.driver.element(self.browser,'xpath', payment_claim.claim_management_list_yj_claimmoney_xpath).send_keys('%s'%self.money_all)
    #     # 认领类型选择“正常”,并点击确定按钮；
    #     get_element.drow_down_input(self.browser,u'认领类型',u'正常')
    #     self.driver.clic(self.browser,'name',payment_claim.claim_management_list_yj_submit_name)
    #     # 选择选择对应的输入框，查询需要认领的订单,验证查询出的数据是否只有一条；
    #     self.driver.element(self.browser,'name',payment_claim.claim_management_sn_name).clear()
    #     self.driver.element(self.browser, 'name', payment_claim.claim_management_sn_name).send_keys(self.ID)
    #     self.driver.clic(self.browser,'name',payment_claim.claim_management_sn_submit_name)
    #     self.page = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_datelist_xpath)
    #     self.assertEqual(public_keyword.page_date_num(self.page), "1")
    #     self.driver.clic(self.browser,'xpath',payment_claim.claim_management_submitclaim_xpath)
    #     # 在认领确认页面，验证认领金额，认领类型，档案编号和借款人姓名是否正确；
    #     self.money = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_money)
    #     self.type = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_type)
    #     self.sn = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_snno)
    #     self.name = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_borrowername)
    #     public_keyword.assert_result(self,public_keyword.number_money(self.money_all),public_keyword.number_money(self.money),text_result=u'认领金额正确；')
    #     # self.assertEqual(public_keyword.number_money(self.money_all),public_keyword.number_money(self.money))
    #     public_keyword.assert_result(self,self.type,u'正常',text_result=u'认领方式为正常认领，正确；')
    #     # self.assertEqual(self.type,u'正常')
    #     self.assertEqual(self.name,self.customerName)
    #     # 认领确认页面，点击确定按钮,验证提示“确认认领成功”
    #     self.driver.clic(self.browser,'name',payment_claim.claim_management_submitclaimcheck_submitname)
    #     self.text = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_submitclaimcheck_promptbox)
    #     self.assertEqual(self.text, u'确认认领成功')
    #     self.logs.info_log(u'4、认领成功后，检查历史认领，各数据是否正确；')
    #     # 检查历史认领记录，是否正常；
    #     get_element.page_enter(self.browser,u'历史认领')
    #     self.driver.element(self.browser, 'name', clients_list.number_input_name).clear()
    #     self.driver.element(self.browser,'name',clients_list.number_input_name).send_keys('%s'%self.ID)
    #     time.sleep(1)
    #     self.driver.clic(self.browser,'css',loan_clients.Filter_clic_css)
    #     # 历史认领中，该订单存在一张认领记录，且金额和认领类型正确
    #     self.page = self.driver.get_text(self.browser,'xpath',payment_claim.claim_management_histroydatas_xpath)
    #     self.assertEqual(public_keyword.page_date_num(self.page), "1")
    #     self.money_01 = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_histroydatasmoney_xpath)
    #     public_keyword.assert_result(self,public_keyword.number_money(self.money_01),public_keyword.number_money(self.money_all),text_result=u'认领金额为一期期还和贷前服务费之和，正确；')
    #     # self.assertEqual(public_keyword.number_money(self.money_01),public_keyword.number_money(self.money_all))
    #     self.type_01 = self.driver.get_text(self.browser, 'xpath',payment_claim.claim_management_histroydatastype_xpath)
    #     self.assertEqual(self.type_01, u'正常')
    #     # 点击查看按钮，进入历史认领详情页，验证各数据是否正确；
    #     self.driver.clic(self.browser,'xpath',payment_claim.claim_management_histroydatastype_button)
    #     self.money_02 = self.driver.get_text(self.browser, 'xpath', payment_claim.claim_management_histroydatasmoney_xpath01)
    #     self.assertEqual(public_keyword.number_money(self.money_01), public_keyword.number_money(self.money_all))
    #     self.type_02 = self.driver.get_text(self.browser, 'xpath',payment_claim.claim_management_histroydatastype_xpath01)
    #     self.assertEqual(self.type_02, u'正常')
    #     self.ID_02 = self.driver.get_text(self.browser, 'xpath',payment_claim.claim_management_histroydatasID_xpath01)
    #     self.assertEqual(self.ID_02, self.ID)
    #     # 进入订单详情页，验证认领数据是否正确；
    #     self.logs.info_log(u'5、进入订单详情页，检查还款信息以及服务费清单数据是否正确；')
    #     self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")
    #     self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
    #     self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
    #     public_keyword.assert_result(self,public_keyword.page_date_num(self.page), "1",text_result=u'还款记录中，历史还款记录为1条，正确；')
    #     # self.assertEqual(public_keyword.page_date_num(self.page), "1")
    #     self.text01 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_way_xpath)
    #     self.assertIn(u'认领',self.text01)
    #     self.text02 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_money_xpath)
    #     public_keyword.assert_result(self,public_keyword.number_money(self.text02), public_keyword.number_money(self.money_all),text_result=u'还款记录中，认领金额为一期期还和贷前服务费和，正确；')
    #     # self.assertEqual(public_keyword.number_money(self.text02), public_keyword.number_money(self.money_all))
    #     # 进入订单详情页，验证服务费清单实收金额是否等于认领金额；
    #     self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
    #     self.assertEqual(public_keyword.number_money(self.dqfy_shishou),public_keyword.number_money(self.dqfy_shishou))
    #     # 验证易捷表，第一期是否已还；
    #     dict_01 = get_element.get_payment_datas(self.browser,u'易捷表')
    #     self.qihuan_ss_money = dict_01[u'第1期-本期合计实收款额']
    #     self.qihuan_qs_money = dict_01[u'第1期-本期合计应收款额']
    #     public_keyword.assert_result(self,public_keyword.number_money(self.qihuan_ss_money),public_keyword.number_money(self.qihuan_qs_money),text_result=u'易捷表，第一期期还金额正确；')
    #     # self.assertEqual(public_keyword.number_money(self.qihuan_ss_money),public_keyword.number_money(self.qihuan_qs_money))

