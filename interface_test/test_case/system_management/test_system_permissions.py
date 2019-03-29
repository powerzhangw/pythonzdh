#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):
    #系统权限_查询角色系统权限
    def test_system_permissions_select_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/role/urls'

        datas = {'roleId':'98ed47d20d9e41638b0f47f510097343'
                 }
        data = json.dumps(datas)
        response = requests.get(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #系统权限_更新角色系统权限
    def test_system_permissions_modify_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/role/urls'

        datas = {'urlIdList':'["1","2"]',
                 'roleId':'002762f5549145ceb036cfee64e9ff7e'
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

