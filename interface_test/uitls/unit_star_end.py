#coding=utf-8
import unittest
import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Test_define(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('开始')
        cls.headers = headers()
    @classmethod
    def tearDownClass(cls):
        print('结束')
    # def setUp(self):
    #     self.header = headers()
    #     print('开始执行')
    #
    # def tearDown(self):
    #
    #     print('执行结束')


def login():

    url = 'http://sso.ejie365.cn/userLogin'
    datas = {"name": "NO00002014",
             "password": "446544",
             "isPhone": "N"}
    data = json.dumps(datas)
    response = requests.post(url, data=data)
    #print response.text
    return response.json()['data']['token']

def headers():

    headers = {'token': '123',
               'Content-Type': 'application/json'}

    return headers