#coding=utf-8
from uitls import get_data
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#命名规范,名字_定位类型


#点击客户管理
clients_management_clic_xpath = "//*[@id=\"tSideMenucustomerList\"]/span"

#点击客户列表
clients_list_clic_id = "tSideMenucustomerList"

#编号 点击编号进入详情页
number_clic_xpath = "//*[text()= " + get_data.get_code() + "]"

#档案编号或借款人姓名 搜索框
number_input_name = "tInputFilter"

#选择贷款产品
product_clic_css = 'div[name = "tSelectproductId"]'
#贷款产品 下拉框
#productSelect_clic_xpath = "//*[text()='房贷一抵']"

#选择资方主体
funder_clic_css = 'div[name = "tSelectfunder"]'
#资方主体 下拉
#funderSelect_clic_xpath = "//*[text()='新网银行']"

#选择还款方式
repaymentMenth_clic_css = 'div[name = "tSelectmethod"]'
#还款方式 下拉框
#repaymentMenthSelect_clic_xpath = "//*[text()='等额本息']"

#选择还款状态
repayStatus_clic_css = 'div[name = "tSelectrepayStatus"]'
#还款状态 下拉框
#repayStatusSelect_clic_xpath = "//*[text()='在贷']"

#选择债权状态
isAdvance_clic_css = 'div[name = "tSelectisAdvance"]'
#债权状态 下拉框
#isAdvanceSelect_clic_xpath = "//*[text()='正常']"

#选择所属大区
area_clic_css = 'div[name = "tSelectarea"]'
#所属大区 下拉框
#areaSelect_clic_xpath = "//*[text()='暴力街区']"

#选择所属城市
City_clic_css = 'div[name = "tSelectCity"]'
#所属城市 下拉框
#CitySelect_clic_xpath = "//*[text()='成都']"

#选择所属部门
department_clic_css = 'div[name = "tSelectDeptName"]'
#所属部门 下拉框
#departmentSelect_clic_xpath = "//*[text()='测试部']"

#筛选
Filter_clic_css = 'button[name = "tBtnFilter"]'
#重置筛选
refilter_clic_css = 'button[name = "tBtnResetFilter"]'







