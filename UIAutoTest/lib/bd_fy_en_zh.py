# -*- coding: utf-8 -*-
# @Author  : powerzhang

# 英文翻译中文

import requests
import json
class FanYizhenenzh():
        def __init__(self,qurey_string):
            self.url = "https://fanyi.baidu.com/transapi"
            self.qurey_string =qurey_string
            self.headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

        def get_post_data(self):
            post_data = {"query":self.qurey_string,
                         "from":"en",
                         "to":"zh"}
            return post_data

        def parse_url(self,url,data):
            res = requests.post(url,data=data,headers=self.headers)
            return res.content.decode()

        def get_ret(self,json_str):
            temp_dict = json.loads(json_str)
            ret = temp_dict["data"][0]["dst"]
            print("{}""{}".format(self.qurey_string,ret))

        def run(self):
            post_data = self.get_post_data()
            json_str =self.parse_url(self.url,post_data)
            self.get_ret(json_str)
if __name__ == "__main__":
        while True:
            query_string = input("请输入你要翻译的内容:")
            fanyi = FanYizhenenzh(query_string)
            fanyi.run()