#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #垫付列表提交审批
    def test_submit_paymentlist(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/submit'

        datas = {'baseId':'1',
                 'planId':'1',
                 'advanceId':'1'
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付列表审批处理
    def test_approve_paymentlist(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/approve'

        datas = {'taskId':'54f8030244f34e4ba734e75fb9adc6fb',
                 'status':'2',
                 'remark':'1'
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付列表重新提交审批
    def test_resubmit_paymentlist(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/resubmit'

        datas = {'taskId':'54f8030244f34e4ba734e75fb9adc6fb'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付列表财务确认
    def test_confirm_paymentlist(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/confirm'

        datas = {'taskId':'54f8030244f34e4ba734e75fb9adc6fb',
                 'status':'1',
                 'recordId':'c48e16aed6ef4c3d87f807edb4d80df7'
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])
