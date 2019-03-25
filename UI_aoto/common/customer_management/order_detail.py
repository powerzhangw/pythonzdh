#coding=utf-8
import sys
from uitls import get_data
reload(sys)
sys.setdefaultencoding('utf8')

#在贷客户订单详情页各数据

#在贷客户详情页-客户名字
customer_name = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[1]/div/div[2]/table/tbody/tr/td[1]/div/span'
#在贷客户详情页-客户贷款资方
customer_capital = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[1]'
#在贷客户详情页-客户贷款金额
customer_amount = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[2]'
#在贷客户详情页-客户贷款周期
customer_cycle = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[2]/td[4]'
#在贷客户详情页-本期还款期数
customer_already_repaid = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[3]'
#在贷客户详情页-客户累计已还本金
customer_repayment_money = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[2]'
#在贷客户详情页-客户累计逾期期数
customer_overdue = '//*[@class="detailItem"]/table[@class="detailTable"]/tbody/tr[4]/td[5]'
#在贷客户详情页-还款信息按钮
customer_repayment_page = '//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[5]'
#在贷客户详情页-还款信息-有多少条还款数据
customer_repayment_page_num = '//*[@class="detailItem2"]/div/div[2]/div[4]/div/div[2]/ul/span'
#在贷客户详情页-服务费清单按钮
customer_fwfqd_xpath = '//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[4]'
#在贷客户详情页-还款管理表按钮
customer_hkgl_xpath = '//*[@class="detailItem2"]/div/div[1]/div/div/div/div/div[3]'




