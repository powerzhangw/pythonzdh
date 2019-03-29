#coding=utf-8
import requests
from uitls import unit_star_end
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_case(unit_star_end.Test_define):

    #初始化用户
    def test_initialize_the_user(self):
        url = 'http://192.168.2.14:8080/internal/common/user/init'

        response = requests.get(url,headers=self.headers)

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #获取参数
    def test_get_params(self):
        url = 'http://192.168.2.14:8080/internal/common/params'

        datas = {'classifyId': '1'}
        data = json.dumps(datas)
        response = requests.get(url, headers=self.headers, data=data)

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #公共接口_获取参数_区
    def test_get_params_areas(self):
        url = 'http://192.168.2.14:8080/internal/common/param/areas'


        response = requests.get(url, headers=self.headers)
        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #公共接口_获取参数_市
    def test_get_params_cities(self):
        url = 'http://192.168.2.14:8080/internal/common/param/cities'

        datas = {'areaId': '1'}
        data = json.dumps(datas)
        response = requests.get(url, headers=self.headers, data=data)

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])

    #公共接口_获取参数_部门
    def test_get_params_dept(self):
        url = 'http://192.168.2.14:8080/internal/common/param/dept'

        datas = {'cityId': '1'}
        data = json.dumps(datas)
        response = requests.get(url, headers=self.headers, data=data)

        self.assertListEqual([1, '成功'], [response.json()['code'], response.json()['msg']])
