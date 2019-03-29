#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #数据权限_查询用户
    def test_data_permissions_select_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/users'

        datas = {'userName':'',
                 'dept':'',
                 'area':'',
                 'city':'',
                 'nextPage':'',
                 'pageLimit':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #数据权限_查询用户数据权限
    def test_select_roles_data_permissions(self):
        url = 'http://192.168.2.14:8080/internal/common/user/organization'

        datas = {'userId':''}
        data = json.dumps(datas)
        response = requests.get(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #数据权限_更新用户数据权限
    def test_modify_roles_data_permissions(self):
        url = 'http://192.168.2.14:8080/internal/common/user/organization'

        datas = {'userId':'',
                 'deptIdList':''
                 }
        data = json.dumps(datas)
        response = requests.put(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #数据权限_删除用户数据权限
    def test_delete_roles_data_permissions(self):
        url = 'http://192.168.2.14:8080/internal/common/user/organization'

        datas = {'userId':''}
        data = json.dumps(datas)
        response = requests.delete(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #数据权限_添加用户
    def test_data_permissions_adduser(self):
        url = 'http://192.168.2.14:8080/internal/common/user'

        datas = {'userId':''}
        data = json.dumps(datas)
        response = requests.put(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #数据权限_复制用户
    def test_data_permissions_copyuser(self):
        url = 'http://192.168.2.14:8080/internal/common/user/copy'

        datas = {'fromId':'',
                 'toId':''
                 }
        data = json.dumps(datas)
        response = requests.put(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #数据权限_添加用户_查询所有角色用户
    def test_data_permissions_addusers(self):
        url = 'http://192.168.2.14:8080/internal/common/user'

        datas = {'userName':''}
        data = json.dumps(datas)
        response = requests.get(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])
