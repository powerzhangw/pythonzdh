#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #角色组管理_查询所有角色组
    def test_roles_management_select_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/roles'

        datas = {'userName':'',
                 'createStart':'',
                 'createEnd':'',
                 'modifiedStart':'',
                 'modifiedEnd':'',
                 'nextPage':'',
                 'pageLimit':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #角色组管理_添加角色组
    def test_roles_management_add_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/role'

        datas = {'roleName':'财务部',
                 'remark':''
                 }
        data = json.dumps(datas)
        response = requests.put(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #角色组管理_添加角色组
    def test_roles_management_modify_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/role'

        datas = {'roleName':'',
                 'remark':''
                 }
        data = json.dumps(datas)
        response = requests.put(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

