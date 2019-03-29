#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #客户列表_获取客户列表
    def test_get_customer_list(self):
        url = 'http://192.168.2.14:8080/internal/core/customs'
        datas = {
            "entity": {
                "deptId": "",
                "funder": "",
                "productId": "",
                "repayStatus": ""
            },
            'type':'',
            #需要链表
            'area':'',
            'city':'',
            'customName':'',
            #数据来源于单点
            'method':'',
            #需要链表
            'isAdvance':'',
            'loanStart':'',
            'loanEnd':'',
            'pageLimit':'',
            'nextPage':''
                }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

