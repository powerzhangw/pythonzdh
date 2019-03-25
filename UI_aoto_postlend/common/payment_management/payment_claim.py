#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 还款管理页面“认领管理”按钮
claim_management_id = 'tSideMenuclaim'
# 还款管理页面“认领列表”按钮
claim_management_list_id = 'tSideMenuclaimclaim-index'
# 还款管理页面“认领列表-易捷”
claim_management_list_yj_xpath = '//*[@name="tTagClaimList"]/div[1]/div/div/div/div/div[2]'
# 还款管理页面“认领列表-资方”
claim_management_list_zf_xpath = '//*[@name="tTagClaimList"]/div[1]/div/div/div/div/div[3]'
#还款管理页面“认领列表-资方-交易摘要、转账类型、户名查询框”
claim_management_list_zf_namequery_name = "tInputFilter"
#还款管理页面“认领列表-资方-筛选查询框”
claim_management_list_zf_submit_name = 'tBtnFilter'
# 还款管理页面“认领列表-易捷认领-批量认领”
claim_management_list_yj_batch_name = 'tBtnClaimEJClaim'
# 还款管理页面“认领列表-易捷认领-全选框”
claim_management_list_yj_allcheck_xpath = '//*[@name="tTableClaimEJ"]/div/div[1]/table/thead/tr/th[1]/div/label/span/input'
# 还款管理页面“认领列表-易捷认领-第一行数据的认领按钮”
claim_management_list_yj_snclaim_xpath = '//*[@name="tTableClaimEJ"]/div/div[2]/table/tbody/tr[1]/td[15]/div/div'
#还款管理页面“认领列表-易捷认领-认领弹出框页面-确认金额输入框”
claim_management_list_yj_claimmoney_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/form/div[8]/div/div/input'
#还款管理页面“认领列表-易捷认领-认领弹出框页面-确定按钮”
claim_management_list_yj_submit_name = 'tBtnClaimManageClaimConfirm'
#还款管理页面“认领列表-易捷认领-认领弹出框页面-确定-档案编号查询框；
claim_management_sn_name = 'tInputFilter'
#还款管理页面“认领列表-易捷认领-认领弹出框页面-确定后，订单查询页面筛选按钮；
claim_management_sn_submit_name = 'tBtnFilter'
#还款管理页面“认领列表-易捷认领-认领弹出框页面-确定后，订单查询页面筛选出的数据；
claim_management_datelist_xpath = '//*[@name="tPaginationCustomer"]/span'
#还款管理页面“认领列表-易捷认领-列表中确认认领按钮
claim_management_submitclaim_xpath = '//*[@name="tTableClaimDetailMatch"]/div[1]/div[2]/table/tbody/tr/td[10]/div'
#还款管理页面“认领列表-易捷认领-确认认领核对页面，确定按钮
claim_management_submitclaimcheck_submitname = 'tBtnClaimManageClaim2Confirm'
#还款管理页面“认领列表-易捷认领-确认认领核对页面-确认金额
claim_management_submitclaimcheck_money = '//*[@name="tTableShowClaimDetailDecide"]/div/div[2]/table/tbody/tr/td[12]/div/span'
#还款管理页面“认领列表-易捷认领-确认认领核对页面-认领类型
claim_management_submitclaimcheck_type = '//*[@name="tTableShowClaimDetailDecide"]/div/div[2]/table/tbody/tr/td[13]/div/span'
#还款管理页面“认领列表-易捷认领-确认认领核对页面-档案编号
claim_management_submitclaimcheck_snno = '//*[@name="tTableShowClaimDetailMatch"]/div/div[2]/table/tbody/tr/td[1]/div/a'
#还款管理页面“认领列表-易捷认领-确认认领核对页面-借款人
claim_management_submitclaimcheck_borrowername = '//*[@name="tTableShowClaimDetailMatch"]/div/div[2]/table/tbody/tr/td[2]/div/span'
#确认认领成功后，弹出框
claim_management_submitclaimcheck_promptbox = '/html/body/div[6]/div/div[1]/div/div[2]'
#历史认领中，当前页存在多少数据
claim_management_histroydatas_xpath = '//*[@name="tPaginationCustomer"]/span'
#历史认领中，已认领金额
claim_management_histroydatasmoney_xpath = '//*[@name="tTableClaimHistory"]/div/div[2]/table/tbody/tr[1]/td[12]/div/span'
#历史认领中，已认领类型
claim_management_histroydatastype_xpath = '//*[@name="tTableClaimHistory"]/div/div[2]/table/tbody/tr[1]/td[13]/div/span'
#历史认领中，第一行查看按钮
claim_management_histroydatastype_button = '//*[@name="tTableClaimHistory"]/div/div[2]/table/tbody/tr[1]/td[14]/div/div/a[1]'
#历史认领详情页中，已认领金额
claim_management_histroydatasmoney_xpath01 = '//*[@name="tTableApprovalDetailDecide"]/div/div[2]/table/tbody/tr/td[12]/div/span'
#历史认领详情页中，已认领类型
claim_management_histroydatastype_xpath01 = '//*[@name="tTableApprovalDetailDecide"]/div/div[2]/table/tbody/tr/td[13]/div/span'
#历史认领详情页中，档案编号
claim_management_histroydatasID_xpath01 = '//*[@name="tTableApprovalDetailMatch"]/div/div[2]/table/tbody/tr/td[1]/div/a'

