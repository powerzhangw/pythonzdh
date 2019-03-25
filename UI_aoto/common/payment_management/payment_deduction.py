#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#放置划扣管理所有信息

#“还款管理”按钮
repayment_button_id = "tTopMenurepayment"
#“划扣管理”按钮
deduction_button_id = "tSideMenudeduct"
#“待还列表”按钮
wait_repayment_listid = "tSideMenudeductdeduct-index"
#待还列表“易捷”页签按钮
wait_repayment_ejiepath = '//*[@name="tTagDeductWait"]/div[1]/div/div/div/div/div[2]'
#待还列表“资方”页签按钮
wait_repayment_zfpath = '//*[@name="tTagDeductWait"]/div[1]/div/div/div/div/div[3]'
#待还列表“正常待还”页签按钮
wait_repayment_normalrepaymentpath = '//*[@name="tTagDeductWait"]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]'
#待还列表“逾期待还”页签按钮
wait_repayment_overduerepaymentpath = '//*[@name="tTagDeductWait"]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[3]'
#待还列表-易捷-正常还款-订单编号查询框
wait_repayment_ordername = 'tInputFilter'
#待还列表-易捷-正常还款-"查询"按钮
wait_repayment_confirmname = 'tBtnFilter'
#待还列表-易捷-正常还款-"划扣"按钮
wait_repayment_deductionpath = '//*[@name = "tTableDeductWaitEJ"]/div/div[2]/table/tbody/tr/td[10]/div/div/a[1]'
##待还列表-易捷-正常还款-应还总额
wait_repayment_yh_money = '//*[@name = "tTableDeductWaitEJ"]/div/div[2]/table/tbody/tr[1]/td[7]/div/span'
##待还列表-易捷-正常还款-预划扣额
wait_repayment_yhk_money = '//*[@name = "tTableDeductWaitEJ"]/div/div[2]/table/tbody/tr[1]/td[8]/div/span'
##待还列表-易捷-正常还款-已还款额
wait_repayment_hk_money = '//*[@name = "tTagDeductWaitEJ"]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/span'
#待还列表-易捷-正常还款-划扣页面-预划扣金额(可输入框)
wait_repayment_yhk_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/form/div[3]/div/div/input'
#待还列表-易捷-正常还款-划扣页面-划扣时间（可选择框）
wait_repayment_hksj_xpath = '//*[@name = "tFormDeductManageClaim"]/div[4]/div/div/div[1]/div/input'
#待还列表-易捷-正常还款-划扣页面-划扣时间(划扣时间下来框的确定按钮)
wait_repayment_hksj_button_xpath = '//*[@name = "tFormDeductManageClaim"]/div[4]/div/div/div[2]/div/div/div/div[4]/button[3]/span'
#待还列表-易捷-正常还款-划扣页面-账户号码下拉框以及下拉选择框；
wait_repayment_zhhm_xpath = '//*[@name = "tFormDeductManageClaim"]/div[5]/div/div/div[1]/div/span'
wait_repayment_zhhm_xpath_01 = '//*[@name = "tFormDeductManageClaim"]/div[5]/div/div/div[2]/ul[2]'
#待还列表-易捷-正常还款-划扣页面-确定按钮
wait_repayment_submit_name = 'tBtnClaimManageClaimConfirm'
#划扣后，提示框
wait_repayment_submitclaimcheck_promptbox = '/html/body/div[6]/div/div[1]/div/div[2]'

#划扣列表-预划扣金额
repayment_list_money_xpath = '//*[@name="tTableDeductListEJ"]/div/div[2]/table/tbody/tr/td[8]/div/span'
#划扣列表-划扣状态
repayment_list_status_xpath = '//*[@name="tTableDeductListEJ"]/div/div[2]/table/tbody/tr/td[10]/div/span'


#历史划扣页面，第一行划扣任务的划扣结果；
repaymenthistroy_list_status_xpath = '//*[@name="tTagDeductHistoryEJ"]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/div'
