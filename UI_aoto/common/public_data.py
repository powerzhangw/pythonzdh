#coding=utf-8
from common.customer_management import clients_list,loan_clients,order_detail
from common.payment_management import payment_deduction
from uitls import get_element,log
from selenium.webdriver.common.keys import Keys
import sys,time
reload(sys)
sys.setdefaultencoding('utf8')
logs = log.log_message()

#命名规范,名字_定位类型

#登录用户名输入框
#login_input_id = "name"
login_input_id = "account"
#登录密码输入框
psssword_input_id = "password"
#登录验证码输入框
verification_input_id = "verification"
#校验码
txtPhoneCertify_input_id = 'txtPhoneCertify'
#登录按钮
login_clic_xpath = "//*[text()=\"登录\"]"

#详细信息部分
#借款金额内容定位
browerAmount_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[2]'
#还款方式 等额本息 定位
RepaymentMethod_text_xpath ='//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[7]'
#合同利率（%/年）定位
contractRate_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[6]'
#借款期限 定位
TermOfLoan_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[4]'
#月综合费率
ComprehensiveRate_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[8]'
#所属城市
city_text_xpath = '//*[@class="detail"]/div[@class="clearfix"]/div[2]'
#所属部门
department_text_xpath = '//*[@class="detail"]/div[@class="clearfix"]/div[3]'
#面审人
salerId_text_xpath = '//*[@class="detail"]/div[@class="clearfix"]/div[4]'
#服务到期日期
ServiceExpirationDate_text_xpath = '//*[@class="detail"]/div[@class="clearfix"]/div[5]'
#1.获取资方主体内容定位
funder_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td '
#2.贷款产品内容 房贷一抵 定位
Loan_products_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[3]'
#3.获取放款日期
loan_Date_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[5]'
#4获取借款到期时间 test_Loan_maturity
Loan_maturity_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[1]'
#5本期期数
Current_period_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[3]'
#6累计逾期次数 test_Cumulative_overdue_frequency
Cumulative_overdue_frequency_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[5]'
#7累计逾期金额 test_Accumulated_overdue_amount
Accumulated_overdue_amount_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[7]'
# 8累计已还本金
Accumulated_principal_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[2]'
#9剩余应还本金 test_Surplus_should_also_be_paid_back.
Surplus_should_also_be_paid_back_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[4]'
#10债券状态 test_Bond_state
Bond_state_text_xpath = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[6]'

#订单详情页-还款信息-还款途径
repayment_way_xpath = '//*[@class="detailItem2"]/div/div[2]/div[4]/div/div[1]/div/div[2]/table/tbody/tr/td[3]/div/span'
#订单详情页-还款信息-还款金额
repayment_money_xpath = '//*[@class="detailItem2"]/div/div[2]/div[4]/div/div[1]/div/div[2]/table/tbody/tr/td[6]/div/span'
#订单详情页-还款信息-是否认领
repayment_whethrcliam_xpath = '//*[@class="detailItem2"]/div/div[2]/div[4]/div/div[1]/div/div[2]/table/tbody/tr/td[7]/div/span'
#订单详情页-还款信息-认领人
repayment_cliamname_xpath = '//*[@class="detailItem2"]/div/div[2]/div[4]/div/div[1]/div/div[2]/table/tbody/tr/td[8]/div/span'
