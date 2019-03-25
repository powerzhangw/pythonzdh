#coding=utf-8
from uitls import unit_star_end
from common import baidu
from uitls import get_element
from uitls import get_data
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_01(unit_star_end.Test_define):

    '''百度首页'''
    def test_00_baidu_index(self):
        '''百度测试'''
        self.logs.info_log(u'百度测试按钮点击')
        get_element.element(self.browser,'id',baidu.baidu_input1_id).send_keys('unittest python')
        get_element.clic(self.browser,'id',baidu.badu_click_id)
        self.assertEqual()

    def test_01_baidu_index(self):
        '''异常测试'''
        self.logs.info_log(u'数据测试')
        #还款方式
        self.repayMethodText = u'等额本息'
        #主借人姓名
        self.customerName = u'琳琳'
        #贷款金额
        self.amount = '100'
        #所属部门
        self.deptID = get_data.config_json()[u'所属部门'][u'产品部']
        #资方主体
        self.funder = get_data.config_json()[u'资方主体'][u'金宝保']
        #贷款产品
        self.productId = get_data.config_json()[u'贷款产品'][u'房贷一抵']
        self.response = get_data.get_datas(self.repayMethodText,self.customerName,self.deptID,self.funder,self.productId,self.amount)







