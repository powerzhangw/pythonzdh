#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #逾期催收催收列表
    def test_except_selectListPage(self):
        url = 'http://192.168.2.14:8080/internal/collection/selectListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'currentOverdueDays':'',
                 'totalOverdueDays':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #催收管理电话催收
    def test_except_phoneSave(self):
        url = 'http://192.168.2.14:8080/internal/collection/phoneSave'

        datas = {'baseId':'1',
                 'collectionDate':'2018-06-25 20:05:22',
                 'collectionName':'1',
                 'isPromise':'1',
                 'paymentType':'',
                 'paymentDate':'',
                 'paymentBank':'',
                 'paymentAccount':'',
                 'paymentName':'',
                 'remark':'',
                 'recordId':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #催收管理线下催收
    def test_except_visitSave(self):
        url = 'http://192.168.2.14:8080/internal/collection/visitSave'

        datas = {'baseId':1,
                 'collectionDate':'2018-06-25 20:05:22',
                 'collectionName':'1',
                 'collectionType':'0014600001',
                 'companyName':'',
                 'companyPhone':'',
                 'companyAddress':'',
                 'interviewDate':'',
                 'interviewNumber':'',
                 'isPromise':1,
                 'paymentType':'',
                 'paymentDate':'',
                 'paymentBank':'',
                 'paymentAccount':'',
                 'paymentName':'',
                 'remark':'',
                 'recordId':'',
                 'attachId':'',
                 'coreCollectionUser':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #催收管理短信催收
    def test_except_smsSave(self):
        url = 'http://192.168.2.14:8080/internal/collection/smsSave'

        datas = {'baseId':'1',
                 'customerName':'1',
                 'telephone':'111',
                 'planTotalNumber':'1',
                 'planOverdueSet':'1',
                 'currentOverdueDays':'1',
                 'currentOverdueMoney':'1',
                 'firstOverdueDate':'2018-06-24 00:00:00',
                 'remark':'1',
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #逾期催收历史催收
    def test_except_selectHistoryListPage(self):
        url = 'http://192.168.2.14:8080/internal/collection/selectHistoryListPage'

        datas = {'nextPage':'1',
                 'pageLimit':'1',
                 'fileNumber':'',
                 'funder':'',
                 'deptId':'',
                 'city':'',
                 'type':'',
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #获取逾期催收短信模板
    def test_except_selectlist(self):
        url = 'http://192.168.2.14:8080/internal/configParam/selectlist'

        datas = {'classifyId':''}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])


