#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #查询所有清贷流程配置
    def test_selectAll_config(self):
        url = 'http://192.168.2.14:8080/internal/configClearParam/selectAll'

        datas = {'isAvailable':''}
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #修改清贷流程配置
    def test_update_config(self):
        url = 'http://192.168.2.14:8080/internal/configClearParam/update'

        datas = {'configId':'',
                 'paramName':'',
                 'paramValueFirst':'',
                 'paramValueFirst': '',
                 'isAvailable':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

