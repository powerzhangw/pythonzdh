#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#命名规范,名字_定位类型



#点击银行卡管理
bankCard_clic_id = "tTopMenubankcard"
#点击公司卡管理
companyCardManagement_clic_id = 'tSideMenucompanyBank'
#姓名、银行卡查询框
nameAndCareSearch_inupt_name = 'tInputFilter'
#账户名称搜索框
accountSearch_clic_name = 'tSelectaccountName'
#开户银行搜索框
AccountOpeningBankSearch_clic_name = 'tSelectaccountBank'
#主要用途搜索框
MainUsesSearch_clic_name = 'tSelectpurpose'
#使用状态搜索框
userStatusSearch_clic_name = 'tSelectstatus'
#筛选按钮 tBtnFilter
filter_cli_name = 'tBtnFilter'
#新增按钮
add_clic_name = 'tTableCompanyBankAdd'
#批量启用按钮
BatchEnabled_clic_name = 'tTableCompanyBankEnable'
#批量停用按钮
BatchDisabled_clic_name = 'tTableCompanyBankDisable'
#批量删除按钮
BatchDelete_clic_name = 'tTableCompanyBankDelete'
#新增-名字输入框
addName_input_css = '.tInputuserName>div>div>input'
#新增-身份证号输入框
addIDCard_input_css = '.tInputuserNo>div>div>input'
#新增-账户名称输入框
addAccount_input_css = '.tInputaccountName>div>div>input'
#新增-银行卡号输入框
addBankCard_input_css = '.tInputcardNum>div>div>input'
#新增开户银行输入框
addOpenAccountCard_input_css = '.tInputbankName>div>div>input'
#新增预留联系电话输入框
addTelephone_input_css = '.tInputtel>div>div>input'
#新增主要用途输入框
addUser_input_css = '.addTelephone_input_css>div>div>div>div>span'
#新增确认
addConfirm_clic_name = 'tBtnConfirmAddBank'