#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')



class Test_case(unit_star_end.Test_define):
    #押品，清贷，倕收，受让暂时没做
    #基本信息
    def test_base_information(self):
        url = 'http://192.168.2.14:8080/internal/core/order/base'

        datas = {'baseId':'4'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #客户信息
    def test_custom_information(self):
        url = 'http://192.168.2.14:8080/internal/core/order/custom'

        datas = {'baseId':'1'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #还款管理表_客户表
    def test_repayment_manage_custom(self):
        url = 'http://192.168.2.14:8080/internal/core/order/plan/custom'

        datas = {'baseId':'1'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #还款管理表_服务方
    def test_repayment_manage_server(self):
        url = 'http://192.168.2.14:8080/internal/core/order/plan/server'

        datas = {'baseId':'3'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #还款管理表_资方表
    def test_repayment_manage_fund(self):
        url = 'http://192.168.2.14:8080/internal/core/order/plan/fund'

        datas = {'baseId':'1'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #服务费清单_贷前服务费
    def test_sever_list_prefee(self):
        url = 'http://192.168.2.14:8080/internal/core/order/prefee'
        headers = {'token':'123',
                   'Content-Type': 'application/json'}
        datas = {'baseId':'1'}
        data = json.dumps(datas)
        response = requests.post(url,headers=headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #服务费清单_贷后服务费
    def test_sever_list_prefee_postlend(self):
        url = 'http://192.168.2.14:8080/internal/core/order/postlend'

        datas = {'baseId':'1'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #还款信息
    def test_repay_information(self):
        url = 'http://192.168.2.14:8080/internal/core/order/repay'

        datas = {'baseId':'1',
                 'nextPage':'',
                 'pageLimit':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #代偿信息
    def test_compfee_information(self):
        url = 'http://192.168.2.14:8080/internal/core/order/compfee'

        datas = {'baseId':''}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #逾期信息
    def test_overdue_information(self):
        url = 'http://192.168.2.14:8080/internal/core/order/overdue'

        datas = {'baseId':'',
                 'nextPage':'',
                 'pageLimit':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付信息
    def test_advance_information(self):
        url = 'http://192.168.2.14:8080/internal/core/order/advance'

        datas = {'baseId':''}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

