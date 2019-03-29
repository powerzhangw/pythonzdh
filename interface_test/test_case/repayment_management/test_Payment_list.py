#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #查询垫付任务列表
    def test_selectListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':'',
                 'status':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #查询待审批垫付任务
    def test_selectManagerListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectManagerListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':'',
                 'status':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付任务已通过列表
    def test_selectPassListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectPassListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':'',
                 'status':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付任务已拒绝列表
    def test_selectRejectListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectRejectListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #查询待确认垫付任务
    def test_selectFinanceListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectFinanceListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #垫付任务已确认列表
    def test_selectConfirmedListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectConfirmedListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #查询历史垫付任务
    def test_selectHistoryListPage_payment(self):
        url = 'http://192.168.2.14:8080/internal/ejieAdvanceTask/selectHistoryListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'area':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

