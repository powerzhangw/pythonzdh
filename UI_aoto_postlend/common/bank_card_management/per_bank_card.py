#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#命名规范,名字_定位类型


#点击银行卡管理
bankCard_clic_id = "tTopMenubankcard"
#点击客户卡管理
CustomerCardManagement_clic_id = 'tSideMenucompanyBank'
#名字搜索框
nameSearch_input_name = 'tInputFilter'
#所属大区搜索框
areaSearch_clic_name = 'tSelectarea'
#所属城市搜索框
citySearch_clic_name = 'tSelectCity'
#所属部门搜索框
partmentSearch_clic_name = 'tSelectDeptName'
#白名单状态搜索框
WhiteListSearch_clic_name = 'tSelectisRegisted'
#使用状态搜索框
userStatusSearch_clic_name = 'tSelectisAvailable'
#筛选按钮
filtter_clic_name = 'tBtnFilter'
#新增按钮
add_clic_name = 'tTableBorrowerBankAdd'
#批量启用
BatchEnabled_clic_name = 'tTableBorrowerBankEnable'
#批量停用按钮
BatchDisabled_clic_name = 'tTableBorrowerBankDisable'
#批量删除按钮
BatchDelete_clic_name = 'tTableBorrowerBankDelete'
#新增档案编号
addFileNumber_input_css = '.tSelectfileNum>div>div>div>div>input'
#新增账户名称
addAccountNames_input_css = '.tInputmaster>div>div>input'
#新增银行卡
addBackCard_input_css = '.tInputnumber>div>div>input'
#新增开户银行
addOpenAccountCard_input_css = '.tInputbranch>div>div>input'
#新增预留联系电话输入框
addTelephone_input_css = '.tInputtel>div>div>input'
#新增确定按钮
addConfirm_clic_name = 'tBtnConfirmAddBank'