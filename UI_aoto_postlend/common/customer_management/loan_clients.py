#coding=utf-8
import sys
from uitls import get_data
reload(sys)
sys.setdefaultencoding('utf8')
#命名规范,名字_定位类型



#点击客户管理
clients_management_clic_xpath = "//*[@id=\"tSideMenucustomerList\"]/span"
clients_management_clic_id = 'tTopMenucustomer'
#点击在贷客户
loan_clients_clic_xpath = "//*[@id=\"tSideMenuloanList\"]/span"

#编号 点击编号进入详情页
number_clic_xpath = "//*[text()= " + get_data.get_code() + "]"

#档案编号或借款人姓名 搜索框
number_input_name = "tInputFilter"

#选择贷款产品
product_clic_css = 'div[name = "tSelectproductId"]'
#product_clic_css = 'tSelectproductId'
#贷款产品 下拉框
#productSelect_clic_xpath = "//*[text()='房贷一抵']"

#选择资方主体
funder_clic_css = 'div[name = "tSelectfunder"]'
#funder_clic_css = 'tSelectfunder'
#资方主体 下拉
#funderSelect_clic_xpath = "//*[text()='新网银行']"

#选择还款方式
repaymentMenth_clic_css = 'div[name = "tSelectmethod"]'
#repaymentMenth_clic_css = 'tSelectmethod'
#还款方式 下拉框
#repaymentMenthSelect_clic_xpath = "//*[text()='等额本息']"

#选择还款状态
repayStatus_clic_css = 'div[name = "tSelectrepayStatus"]'
#repayStatus_clic_css = 'tSelectrepayStatus'
#还款状态 下拉框
#repayStatusSelect_clic_xpath = "//*[text()='在贷']"

#选择债权状态
isAdvance_clic_css = 'div[name = "tSelectisAdvance"]'
#isAdvance_clic_css = 'tSelectisAdvance'
#债权状态 下拉框
#isAdvanceSelect_clic_xpath = "//*[text()='正常']"

#选择所属大区
area_clic_css = 'div[name = "tSelectarea"]'
#area_clic_css = 'tSelectarea'
#所属大区 下拉框
#areaSelect_clic_xpath = "//*[text()='暴力街区']"

#选择所属城市
City_clic_css = 'div[name = "tSelectCity"]'
#City_clic_css = 'tSelectCity'
#所属城市 下拉框
#CitySelect_clic_xpath = "//*[text()='成都']"

#选择所属部门
department_clic_css = 'div[name = "tSelectDeptName"]'
#department_clic_css = 'tSelectDeptName'
#所属部门 下拉框
#departmentSelect_clic_xpath = "//*[text()='测试部']"

#筛选
Filter_clic_css = 'button[name = "tBtnFilter"]'
#重置筛选
refilter_clic_css = 'button[name = "tBtnResetFilter"]'

#在贷客户列表，第一条数据的id
order_id_xpath = '//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr/td[1]/div'

#点击操作
operate_clic_xpath  = '//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr[1]/td[12]/div/div/div[1]/i'
#发起垫付
payment_clic_xpath = '//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr[1]/td[12]/div/div/div[2]/ul/li[1]'
#发起清贷
ClearLoan_clic_xpath = '//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr[1]/td[12]/div/div/div[2]/ul/li[3]'
#发起受让
assignee_clic_xpath = '//*[@name="tTableLoanList"]/div/div[2]/table/tbody/tr[1]/td[12]/div/div/div[2]/ul/li[2]'


