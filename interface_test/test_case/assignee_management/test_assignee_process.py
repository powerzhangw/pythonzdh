#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #受让列表提交审批
    def test_assigneelist_submit(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/submit'

        datas = {'baseId':'945d2dfd94154662901d1ecebbec38ab',
                 'buyBackId':'',
                 'attachId':'',
                 'reasonType':1,
                 'reasonDesc':'',
                 'directorId':'945d2dfd94154662901d1ecebbec38aa',
                 'viceId':'945d2dfd94154662901d1ecebbec38ab',
                 'presidentId':'945d2dfd94154662901d1ecebbec38ac'
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #受让列表审批处理
    def test_assigneelist_approve(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/approve'

        datas = {'taskId':'',
                 'status':'',
                 'remark':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #受让列表重新发起审批
    def test_assigneelist_resubmit(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/resubmit'

        datas = {'taskId':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #受让列表财务确认
    def test_assigneelist_confirm(self):
        url = 'http://192.168.2.14:8080/internal/ejieBuyBackTask/confirm'

        datas = {'taskId':'',
                 'recordId':'',
                 'status':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

