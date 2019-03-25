# coding=utf-8
from uitls import unit_star_end,get_element,get_data
from common.customer_management import clients_list,loan_clients,order_detail
from common.payment_management import payment_deduction,payment_claim
from common import public_data,public_keyword
from selenium.webdriver.common.keys import Keys
import sys,time,random
reload(sys)
sys.setdefaultencoding('utf8')

class Test_01(unit_star_end.Test_define):

    '''在贷客户进行划扣操作'''
    def test_01_deduction_index(self):
        '''验证新进订单，进单日期为当前日期，进行贷前划扣操作'''
        self.logs.info_log(u'验证新进订单，进单日期为当前日期，进行贷前划扣操作；')
        self.logs.info_log(u'1、使用接口进单；')
        # 还款方式
        self.repayMethodText = u'等额本息'
        # 主借人姓名
        self.customerName = unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5))
        # 贷款金额
        self.amount = int('30')
        # 划扣金额
        self.claimmoney = '100'
        # 当前已还款金额
        self.alreadystillmoney = '0'
        #还款信息条数
        self.nber = '0'
        # 所属部门
        self.deptID = self.get_datas.config_json()[u'所属部门'][u'成都房贷一部']
        # 资方主体
        self.funder = self.get_datas.config_json()[u'资方主体'][u'外贸信托']
        self.funderProductConfig = self.get_datas.config_json()[u'资方'][u'测试资方']
        #进件时间
        t1 = int(time.time())
        t2 = str(t1) + '000'
        time1 = int(t2)
        # 贷款产品
        self.productId = self.get_datas.config_json()[u'贷款产品'][u'房贷一抵']
        self.response = self.get_datas.get_datas(self.repayMethodText, self.customerName, self.deptID, self.funder,
                                           self.productId, self.amount,self.get_datas.get_code(),self.funderProductConfig,time1)
        self.assertEqual(self.response,u'成功')
        #获取订单id号
        self.ID = get_element.order_sn_id(self.browser, self.customerName)
        #进入订单详情页
        get_element.order_details_page(self.browser, self.ID)
        #验证订单各数据是否正确；
        self.logs.info_log(u'2、获取订单相关信息，验证金额、客户名、当前贷款期限、当前还款信息等是否正确；')
        #验证客户姓名是否正确
        self.customer_name = get_element.get_text(self.browser,'xpath','%s'%order_detail.customer_name)
        # self.customer_name = self.driver.get_text(self.browser,'xpath','%s'%order_detail.customer_name)
        public_keyword.assert_result(self,self.customerName,self.customer_name,text_result=u'进单客户和订单实际客户正确')
        # self.assertEqual(self.customerName,self.customer_name)
        #验证贷款金额是否正确
        self.customer_amount = self.driver.get_text(self.browser,'xpath',order_detail.customer_amount)
        public_keyword.assert_result(self,public_keyword.number_money(self.customer_amount),float(self.amount*10000),text_result=u'贷款金额正确')
        # self.assertEqual(public_keyword.number_money(self.customer_amount),float(self.amount*10000))
        #验证当前还款期限是否为第一期
        self.customer_repaid_now = self.driver.get_text(self.browser,'xpath',order_detail.customer_already_repaid)
        #点击还款信息,验证当前还款信息为0
        self.driver.clic(self.browser,'xpath',order_detail.customer_repayment_page)
        self.page = self.driver.get_text(self.browser,'xpath',order_detail.customer_repayment_page_num)
        public_keyword.assert_result(self,public_keyword.page_date_num(self.page),self.nber,text_result=u'订单当前还款信息为0')
        # self.assertEqual(public_keyword.page_date_num(self.page),self.nber)
        #查询贷前费用实收总和；
        self.dqfy_shishou = public_keyword.ss_service_money(self,self.ID)
        #查询贷前费用应收总和；
        self.dqfy_yinshou = public_keyword.ys_service_money(self, self.ID)
        #完善银行卡信息
        text = public_keyword.edit_bankcard(self, self.customerName)
        public_keyword.assert_result(self,text, u'更新客户银行卡成功',text_result=u'更新银行卡成功')
        # self.assertEqual(text, u'更新客户银行卡成功')
        self.logs.info_log(u'3、还款管理页面，进入划扣页面，进行划扣操作；')
        # 进行划扣操作
        deduction_dict = public_keyword.deduction_money(self,ID='%s'%self.ID,claim_money='%s'%self.claimmoney,zifang=u'易捷',hklx=u'正常待还',czuo=u'划扣')
        public_keyword.assert_result(self,public_keyword.number_money(deduction_dict[u'应还总额']), public_keyword.number_money(self.dqfy_yinshou),text_result=u'订单应还总额正确')
        # self.assertEqual(public_keyword.number_money(deduction_dict[u'应还总额']), public_keyword.number_money(self.dqfy_yinshou))
        self.logs.info_log(u'3.1、还款管理页面，应还金额等于贷前费用总额；')
        public_keyword.assert_result(self,public_keyword.number_money(deduction_dict[u'预划扣额']), float(0) ,text_result=u'预划扣金额正确')
        # self.assertEqual(public_keyword.number_money(deduction_dict[u'预划扣额']), float(0))
        self.logs.info_log(u'3.2、还款管理页面，预还款金额等于0；')
        public_keyword.assert_result(self,deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功',text_result=u'提交资方划扣任务成功')
        # self.assertEqual(deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功')
        self.logs.info_log(u'3.3、还款管理页面，提交划扣任务成功；')
        # 进入划扣列表查询划扣状态；
        for i in range(30):
            self.text = public_keyword.deduction_recordlist(self, ID=self.ID)
            if self.text == u'订单不存在':
                break
            else:
                time.sleep(10)
        #进入划扣历史；
        for i in range(6):
            self.text01 = public_keyword.deduction_recordhistroy(self,ID=self.ID)
            self.logs.info_log(self.text01)
            if self.text01[u'预划扣状态'] == u"扣款成功":
                self.logs.info_log(u"3.4、划扣历史页面，划扣成功")
                break
            else:
                self.logs.info_log(u"划扣历史页面，划扣失败，重新进行划扣操作")
                deduction_dict = public_keyword.deduction_money(self, ID=self.ID, claim_money=self.claimmoney,zifang=u'易捷', hklx=u'正常待还', czuo=u'划扣')
                public_keyword.assert_result(self, deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功', text_result=u'提交资方划扣任务成功')
                # self.assertEqual(deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功')
                self.logs.info_log(u'第%s次划扣，还款管理页面，提交划扣任务成功'%i)
                for i in range(30):
                    self.text02 = public_keyword.deduction_recordlist(self, ID=self.ID)
                    if self.text02 == u'订单不存在':
                        self.logs.info_log(u'订单划扣结果成功；')
                        break
                    else:
                        time.sleep(10)
        #进入订单详情页，验证认领数据是否正确；
        self.logs.info_log(u'4、进入订单详情页，检查还款信息以及服务费清单数据是否正确；')
        get_element.order_details_page(self.browser, self.ID)
        # self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")
        self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
        self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
        public_keyword.assert_result(self,public_keyword.page_date_num(self.page), "1" , text_result=u'订单详情页，还款记录正确')
        # self.assertEqual(public_keyword.page_date_num(self.page), "1")
        self.text01 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_way_xpath)
        public_keyword.assert_result(self,u'服务方-划扣',self.text01,text_result=u'订单详情页，还款记录为服务费划扣，结果正确')
        # self.assertIn(u'划扣',self.text01)
        self.text02 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_money_xpath)
        public_keyword.assert_result(self,public_keyword.number_money(self.text02), public_keyword.number_money(self.claimmoney) , text_result=u'订单详情页，还款金额正确')
        # self.assertEqual(public_keyword.number_money(self.text02), public_keyword.number_money(self.claimmoney))
        #进入订单详情页，验证服务费清单实收金额是否等于认领金额；
        self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
        public_keyword.assert_result(self,public_keyword.number_money(self.dqfy_shishou),public_keyword.number_money(self.claimmoney),text_result=u'订单详情页，服务费清单还款正确')
        # self.assertEqual(public_keyword.number_money(self.dqfy_shishou),public_keyword.number_money(self.claimmoney))

    def test_02_deduction_index(self):
        '''验证新进订单，进单日期为一个月前日期，进行划扣（第一期期收和贷前费用）操作；'''
        self.logs.info_log(u'验证新进订单，进单日期为一个月前日期，进行划扣（第一期期收和贷前费用）操作；')
        self.logs.info_log(u'1、使用接口进单；')
        # 还款方式
        self.repayMethodText = u'等额本息'
        # 主借人姓名
        self.customerName = unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5))
        # 贷款金额
        self.amount = int('30')
        # 划扣金额
        self.claimmoney = '100'
        # 当前已还款金额
        self.alreadystillmoney = '0'
        #还款信息条数
        self.nber = '0'
        # 所属部门
        self.deptID = self.get_datas.config_json()[u'所属部门'][u'成都房贷一部']
        # 资方主体
        self.funder = self.get_datas.config_json()[u'资方主体'][u'外贸信托']
        self.funderProductConfig = self.get_datas.config_json()[u'资方'][u'测试资方']
        #进件时间
        t1 = int(time.time()) - int(2419200)
        t2 = str(t1) + '000'
        time1 = int(t2)
        # 贷款产品
        self.productId = self.get_datas.config_json()[u'贷款产品'][u'房贷一抵']
        self.response = self.get_datas.get_datas(self.repayMethodText, self.customerName, self.deptID, self.funder,
                                           self.productId, self.amount,self.get_datas.get_code(),self.funderProductConfig,time1)
        self.assertEqual(self.response,u'成功')
        #获取订单id号并跑批
        self.ID = get_element.order_sn_id(self.browser, self.customerName)
        self.response = get_data.batch_task('%s' % self.ID)
        self.assertEqual(self.response, u'成功')
        #进入订单详情页
        get_element.order_details_page(self.browser, self.ID)
        #验证订单各数据是否正确；
        self.logs.info_log(u'2、获取订单相关信息，验证金额、客户名、当前贷款期限、当前还款信息等是否正确；')
        #验证客户姓名是否正确
        self.customer_name = self.driver.get_text(self.browser,'xpath',order_detail.customer_name)
        public_keyword.assert_result(self,self.customerName,self.customer_name,text_result=u'订单客户名正确；')
        # self.assertEqual(self.customerName,self.customer_name)
        #验证贷款金额是否正确
        self.customer_amount = self.driver.get_text(self.browser,'xpath',order_detail.customer_amount)
        public_keyword.assert_result(self,public_keyword.number_money(self.customer_amount),float(self.amount*10000),text_result=u'贷款金额正确')
        # self.assertEqual(public_keyword.number_money(self.customer_amount),float(self.amount*10000))
        #验证当前还款期限是否为第一期
        self.customer_repaid_now = self.driver.get_text(self.browser,'xpath',order_detail.customer_already_repaid)
        #点击还款信息,验证当前还款信息为0
        self.driver.clic(self.browser,'xpath',order_detail.customer_repayment_page)
        self.page = self.driver.get_text(self.browser,'xpath',order_detail.customer_repayment_page_num)
        public_keyword.assert_result(self,public_keyword.page_date_num(self.page),self.nber,text_result=u'当前还款信息为0，正确')
        # self.assertEqual(public_keyword.page_date_num(self.page),self.nber)
        #查询贷前费用实收总和；
        self.dqfy_shishou = public_keyword.ss_service_money(self,self.ID)
        #查询贷前费用应收总和；
        self.dqfy_yinshou = public_keyword.ys_service_money(self, self.ID)
        #查询借款人表第一期期还的金额以及；
        dict_01 = get_element.get_payment_datas(self.browser, u'易捷表')
        self.qihuan_money = dict_01[u'第1期-本期合计应收款额']
        self.qihuan = public_keyword.number_money(self.qihuan_money)
        self.claim_money = self.qihuan + public_keyword.number_money(self.dqfy_yinshou)
        #完善银行卡信息
        text = public_keyword.edit_bankcard(self, self.customerName)
        public_keyword.assert_result(self,text, u'更新客户银行卡成功',text_result=u'更新银行卡成功')
        # self.assertEqual(text, u'更新客户银行卡成功')
        self.logs.info_log(u'3、还款管理页面，进入划扣页面，进行划扣操作，划扣金额为第一期期还和贷前费用和；')
        # 进行划扣操作
        deduction_dict = public_keyword.deduction_money(self,ID=self.ID,claim_money=self.claim_money,zifang=u'易捷',hklx=u'正常待还',czuo=u'划扣')
        public_keyword.assert_result(self,public_keyword.number_money(deduction_dict[u'应还总额']), self.claim_money,text_result=u'应还金额等于贷前费用和第一期期收金额和，正确')
        # self.assertEqual(public_keyword.number_money(deduction_dict[u'应还总额']), self.claim_money)
        self.logs.info_log(u'3.1、还款管理页面，应还金额等于贷前费用和第一期期收金额和；')
        public_keyword.assert_result(self,public_keyword.number_money(deduction_dict[u'预划扣额']), float(0),text_result=u'还款管理页面，预还款金额等于0,正确')
        # self.assertEqual(public_keyword.number_money(deduction_dict[u'预划扣额']), float(0))
        self.logs.info_log(u'3.2、还款管理页面，预还款金额等于0；')
        public_keyword.assert_result(self,deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功',text_result=u'还款管理页面，提交划扣任务成功')
        # self.assertEqual(deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功')
        self.logs.info_log(u'3.3、还款管理页面，提交划扣任务成功；')
        # 进入划扣列表查询划扣状态；
        for i in range(30):
            self.text = public_keyword.deduction_recordlist(self, ID=self.ID)
            if self.text == u'订单不存在':
                break
            else:
                time.sleep(10)
        #进入划扣历史；
        for i in range(10):
            self.text01 = public_keyword.deduction_recordhistroy(self,ID=self.ID)
            self.logs.info_log(self.text01)
            if self.text01[u'预划扣状态'] == u"扣款成功":
                self.logs.info_log(u"3.4、划扣历史页面，划扣成功")
                break
            else:
                self.logs.info_log(u"划扣历史页面，划扣失败，重新进行划扣操作")
                deduction_dict = public_keyword.deduction_money(self, ID=self.ID, claim_money=self.claim_money,zifang=u'易捷', hklx=u'正常待还', czuo=u'划扣')
                public_keyword.assert_result(self, deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功',text_result=u'还款管理页面，提交划扣任务成功')
                # self.assertEqual(deduction_dict[u'划扣结果'], u'提交服务方划扣任务成功')
                self.logs.info_log(u'第%s次划扣，还款管理页面，提交划扣任务成功'%i)
                for i in range(30):
                    self.text02 = public_keyword.deduction_recordlist(self, ID=self.ID)
                    if self.text02 == u'订单不存在':
                        self.logs.info_log(u'订单划扣结果成功；')
                        break
                    else:
                        time.sleep(10)
        #进入订单详情页，验证认领数据是否正确；
        self.logs.info_log(u'4、进入订单详情页，检查还款信息以及服务费清单数据是否正确；')
        get_element.order_details_page(self.browser, self.ID)
        # self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")
        self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
        self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
        public_keyword.assert_result(self,public_keyword.page_date_num(self.page), "1",text_result=u'还款记录显示为1，正确；')
        # self.assertEqual(public_keyword.page_date_num(self.page), "1")
        self.text01 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_way_xpath)
        public_keyword.assert_result(self,u'服务方-划扣',self.text01,text_result=u'还款记录还款方式为服务方划扣，正确')
        # self.assertIn(u'划扣',self.text01)
        self.text02 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_money_xpath)
        public_keyword.assert_result(self,public_keyword.number_money(self.text02), self.claim_money,text_result=u'还款记录中，还款金额正确；')
        # self.assertEqual(public_keyword.number_money(self.text02), self.claim_money)
        #进入订单详情页，验证服务费清单实收金额是否等于认领金额；
        self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
        public_keyword.assert_result(self,public_keyword.number_money(self.dqfy_shishou),self.dqfy_yinshou,text_result=u'贷前服务费，期收和实收相等，正确')
        # self.assertEqual(public_keyword.number_money(self.dqfy_shishou),self.dqfy_yinshou)
        # 验证易捷表，第一期是否已还；
        dict_01 = get_element.get_payment_datas(self.browser, u'易捷表')
        self.qihuan_ss_money = dict_01[u'第1期-本期合计实收款额']
        self.qihuan_qs_money = dict_01[u'第1期-本期合计应收款额']
        public_keyword.assert_result(self,public_keyword.number_money(self.qihuan_ss_money),public_keyword.number_money(self.qihuan_qs_money),text_result=u'易捷表，一期实还和待还相等，正确；')
        # self.assertEqual(public_keyword.number_money(self.qihuan_ss_money),public_keyword.number_money(self.qihuan_qs_money))

    def test_03_deduction_index(self):
        '''验证新进订单，进单日期为当前日期，进行资方划扣操作'''
        self.logs.info_log(u'验证新进订单，进行资方划扣操作；')
        self.logs.info_log(u'1、使用接口进单；')
        # 还款方式
        self.repayMethodText = u'等额本息'
        # 主借人姓名
        self.customerName = unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5)) + unichr(random.randint(0x4e00,0x9fa5))
        # 贷款金额
        self.amount = int('30')
        # 划扣金额
        self.claimmoney = '100'
        # 当前已还款金额
        self.alreadystillmoney = '0'
        #还款信息条数
        self.nber = '0'
        # 所属部门
        self.deptID = self.get_datas.config_json()[u'所属部门'][u'成都房贷一部']
        # 资方主体
        self.funder = self.get_datas.config_json()[u'资方主体'][u'外贸信托']
        self.funderProductConfig = self.get_datas.config_json()[u'资方'][u'测试资方']
        #进件时间
        t1 = int(time.time()) - int(2419200)
        t2 = str(t1) + '000'
        time1 = int(t2)
        # 贷款产品
        self.productId = self.get_datas.config_json()[u'贷款产品'][u'房贷一抵']
        self.response = self.get_datas.get_datas(self.repayMethodText, self.customerName, self.deptID, self.funder,
                                           self.productId, self.amount,self.get_datas.get_code(),self.funderProductConfig,time1)
        self.assertEqual(self.response,u'成功')
        #获取订单id号并跑批
        self.ID = get_element.order_sn_id(self.browser, self.customerName)
        self.response = get_data.batch_task('%s' % self.ID)
        self.assertEqual(self.response, u'成功')
        #进入订单详情页
        get_element.order_details_page(self.browser, self.ID)
        #验证订单各数据是否正确；
        self.logs.info_log(u'2、获取订单相关信息，验证金额、客户名、当前贷款期限、当前还款信息等是否正确；')
        #验证客户姓名是否正确
        self.customer_name = self.driver.get_text(self.browser,'xpath',order_detail.customer_name)
        public_keyword.assert_result(self, self.customerName,self.customer_name,text_result=u'订单客户姓名正确')
        # self.assertEqual(self.customerName,self.customer_name)
        #验证贷款金额是否正确
        self.customer_amount = self.driver.get_text(self.browser,'xpath',order_detail.customer_amount)
        public_keyword.assert_result(self,public_keyword.number_money(self.customer_amount),float(self.amount*10000),text_result=u'订单金额正确')
        # self.assertEqual(public_keyword.number_money(self.customer_amount),float(self.amount*10000))
        #验证当前还款期限是否为第一期
        self.customer_repaid_now = self.driver.get_text(self.browser,'xpath',order_detail.customer_already_repaid)
        #点击还款信息,验证当前还款信息为0
        self.driver.clic(self.browser,'xpath',order_detail.customer_repayment_page)
        self.page = self.driver.get_text(self.browser,'xpath',order_detail.customer_repayment_page_num)
        public_keyword.assert_result(self,public_keyword.page_date_num(self.page),self.nber,text_result=u'还款信息表，当前还款信息为0，正确')
        # self.assertEqual(public_keyword.page_date_num(self.page),self.nber)
        #查询贷前费用实收总和；
        self.dqfy_shishou = public_keyword.ss_service_money(self,self.ID)
        #查询贷前费用应收总和；
        self.dqfy_yinshou = public_keyword.ys_service_money(self, self.ID)
        #查询借款人表第一期期还的金额以及；
        dict_01 = get_element.get_payment_datas(self.browser,u'资方表')
        self.qihuan_money = dict_01[u'第1期-本期合计应还款额']
        self.claim_money = public_keyword.number_money(self.qihuan_money)
        #完善银行卡信息
        text = public_keyword.edit_bankcard(self, self.customerName)
        self.assertEqual(text, u'更新客户银行卡成功')
        self.logs.info_log(u'3、还款管理页面，进入划扣页面，进行划扣操作，划扣金额为第一期期还和贷前费用和；')
        # 进行划扣操作，进行资方划扣
        deduction_dict = public_keyword.deduction_money(self, ID=self.ID, claim_money=self.claim_money, zifang=u'资方',hklx=None, czuo=u'划扣')
        # self.assertEqual(public_keyword.number_money(deduction_dict[u'应还总额']), self.claim_money)
        public_keyword.assert_result(self,public_keyword.number_money(deduction_dict[u'应还总额']), self.claim_money,text_result=u'应还金额等于贷前费用和第一期期收金额和，正确；')
        self.logs.info_log(u'3.1、还款管理页面，应还金额等于贷前费用和第一期期收金额和；')
        public_keyword.assert_result(self,public_keyword.number_money(deduction_dict[u'预划扣额']), float(0),text_result=u'划扣页面，预划扣金额为0，正确；')
        # self.assertEqual(public_keyword.number_money(deduction_dict[u'预划扣额']), float(0))
        self.logs.info_log(u'3.2、还款管理页面，预还款金额等于0；')
        public_keyword.assert_result(self,deduction_dict[u'划扣结果'], u'提交资方划扣任务成功',text_result=u'提交资方划扣任务成功，正确；')
        # self.assertEqual(deduction_dict[u'划扣结果'], u'提交资方划扣任务成功')
        self.logs.info_log(u'3.3、还款管理页面，提交划扣任务成功；')
        # 进入划扣列表查询划扣状态；

        for i in range(30):
            self.text = public_keyword.deduction_recordlist(self, ID=self.ID,text=u'资方',hklx=None)
            if self.text == u'订单不存在':
                break
            else:
                time.sleep(10)

        #进入划扣历史；
        for i in range(10):
            self.text01 = public_keyword.deduction_recordhistroy(self,ID=self.ID,text=u'资方',hklx = None)
            self.logs.info_log(self.text01)
            if self.text01[u'预划扣状态'] == u"扣款成功":
                self.logs.info_log(u"3.4、划扣历史页面，划扣成功")
                break
            else:
                self.logs.info_log(u"划扣历史页面，划扣失败，重新进行划扣操作")
                deduction_dict = public_keyword.deduction_money(self, ID=self.ID, claim_money=self.claim_money,zifang=u'资方', hklx=None, czuo=u'划扣')
                public_keyword.assert_result(self, deduction_dict[u'划扣结果'], u'提交资方划扣任务成功',text_result=u'提交资方划扣任务成功，正确；')
                # self.assertEqual(deduction_dict[u'划扣结果'], u'提交资方划扣任务成功')
                self.logs.info_log(u'第%s次划扣，还款管理页面，提交划扣任务成功'%i)
                time.sleep(120)
                for i in range(30):
                    self.text02 = public_keyword.deduction_recordlist(self, ID=self.ID,text=u'资方',hklx = None)
                    if self.text02 == u'订单不存在':
                        self.logs.info_log(u'订单划扣结果成功；')
                        break
                    else:
                        time.sleep(10)
        #进入订单详情页，验证认领数据是否正确；
        self.logs.info_log(u'4、进入订单详情页，检查还款信息以及服务费清单数据是否正确；')
        get_element.order_details_page(self.browser, self.ID)
        # self.driver.clic(self.browser, 'xpath', "//*[text()= " + self.ID + "]")
        self.driver.clic(self.browser, 'xpath', order_detail.customer_repayment_page)
        self.page = self.driver.get_text(self.browser, 'xpath', order_detail.customer_repayment_page_num)
        public_keyword.assert_result(self,public_keyword.page_date_num(self.page), "1",text_result=u'还款记录列表，还款记录为1，正确；')
        # self.assertEqual(public_keyword.page_date_num(self.page), "1")
        self.text01 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_way_xpath)
        public_keyword.assert_result(self, u'资方-划扣',self.text01,text_result=u'还款记录列表，还款方式为资方划扣，正确；')
        # self.assertIn(u'资方-划扣',self.text01)
        self.text02 = self.driver.get_text(self.browser, 'xpath', public_data.repayment_money_xpath)
        public_keyword.assert_result(self, public_keyword.number_money(self.text02), self.claim_money,text_result=u'还款记录列表，还款金额等于划扣金额，正确；')
        # self.assertEqual(public_keyword.number_money(self.text02), self.claim_money)
        #进入订单详情页，验证服务费清单实收金额是否等于认领金额；
        self.dqfy_shishou = public_keyword.ss_service_money(self, self.ID)
        public_keyword.assert_result(self,public_keyword.number_money(self.dqfy_shishou),self.dqfy_yinshou,text_result=u'贷前费用期收等于实收，正确；')
        # self.assertEqual(public_keyword.number_money(self.dqfy_shishou),self.dqfy_yinshou)
        # 验证易捷表，第一期是否已还；
        dict_01 = get_element.get_payment_datas(self.browser,u'资方表')
        self.qihuan_ss_money = dict_01[u'第1期-本期合计应还款额']
        self.qihuan_qs_money = dict_01[u'第1期-本期合计实还款额']
        public_keyword.assert_result(self,public_keyword.number_money(self.qihuan_ss_money),public_keyword.number_money(self.qihuan_qs_money),text_result=u'易捷表，第一期期还和实还相等，正确；')
        # self.assertEqual(public_keyword.number_money(self.qihuan_ss_money),public_keyword.number_money(self.qihuan_qs_money))


