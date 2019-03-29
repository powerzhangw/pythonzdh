#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):

    #菜单权限_查询角色菜单权限
    def test_menu_permissions_select_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/role/menus'

        datas = {'roleId':'财务部'}
        data = json.dumps(datas)
        response = requests.get(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #菜单权限_更新角色菜单权限
    def test_menu_permissions_modify_roles(self):
        url = 'http://192.168.2.14:8080/internal/common/role/menus'

        datas = {'roleID':'',
                 'menuIdList':''
                 }
        data = json.dumps(datas)
        response = requests.post(url,headers=self.headers,data=data )

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

