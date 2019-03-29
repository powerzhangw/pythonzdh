#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Test_case(unit_star_end.Test_define):
    #查询受让任务列表
    def test_assignee_selectListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectListPage'
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
        print response.json()['code']
        print response.json()['msg']
        #self.assertEqual(1,response.json()['code'])
        self.assertListEqual([1,'成功'],[response.json()['code'],response.json()['msg']])

    #查询总监审批列表
    def test_assignee_selectDirectorListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectDirectorListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        # self.assertEqual(1,response.json()['code'])
        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #区域副总审批列表
    def test_assignee_selectViceListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectViceListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #总经理审批列表
    def test_assignee_selectPresidentListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectPresidentListPage'
        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #已通过流水历史列表
    def test_assignee_selectPassListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectPassListPage'
        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'beginTime':'',
                 'endTime':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #已拒绝流水历史列表
    def test_assignee_selectRejectListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectRejectListPage'
        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'beginTime':'',
                 'endTime':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #受让列表财务待确认列表
    def test_assignee_selectFinanceListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectFinanceListPage'
        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #财务已确认历史列表
    def test_assignee_selectConfirmedListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectConfirmedListPage'
        datas = {'nextPage': '1',
                 'pageLimit': '1',
                 'fileNumber': '',
                 'funder': '',
                 'deptId': '',
                 'beginTime': '',
                 'endTime': ''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #查询历史受让任务
    def test_assignee_selectHistoryListPage(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectHistoryListPage'
        datas = {'nextPage': '1',
                 'pageLimit': '1',
                 'fileNumber': '',
                 'funder': '',
                 'deptId': '',
                 'city': '',
                 'area': '',
                 'status':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #查询受让任务详细
    def test_assignee_selectDetail(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/selectDetail'
        datas = {'buyBackId': '945d2dfd94154662901d1ecebbec38ab'}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])


