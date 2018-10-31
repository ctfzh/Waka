# -*- coding: UTF-8 -*-
import requests
import json
import readConfig as readConfig


class ConfigHttp:
    def __init__(self):
        config = readConfig.ReadConfig()
        global host, port, timeout
        # host = config.get_http("quota_url")
        # port = config.get_http("port")
        timeout = config.get_http("timeout")
        self.headers = {}
        self.params = {}
        self.data = {}
        self.json = {}
        self.url = {}
        self.files = {}

    # request对象的URL
    def set_url(self, url):
        self.url = url

    # 可选的，用于编写http头信息
    def set_headers(self, header):
        self.headers = header

    # 可选的，要在查询字符串中发送的字典或字节request
    def set_params(self, param):
        self.params = param

    # 可选的，字典或元祖列表以表单编码，字节或类似文件的对象在主体中发送[(key,value)]
    def set_data(self, data):
        self.data = data

    # 可选的，一个json可序列化的python对象，在主体中发送request
    def set_json(self, jsons):
        self.json = jsons

    # 可选的，用于多部分编码上传的字典，可以是多元祖，其中是定义给定文件的内容类型的字符串，
    # 以及包含问文件添加的额外头文件的类字典对象
    def set_files(self, file):
        self.files = file

    def get_dict(self):
        try:
            response = requests.request("GET", self.url, params=self.params,
                                        headers=self.headers, timeout=float(timeout))
            response_code = response.status_code
            response_text = json.loads(response.text)
            print("===============================================================")
            print(response_text)
            print("===============================================================")
            return response_code, response_text
        except TimeoutError:
            print("Time out!")
            return None

    def post_dict(self):
        try:
            response = requests.request("POST", self.url, headers=self.headers, json=self.json,
                                        params=self.params, data=self.data, files=self.files)
            response_code = response.status_code
            response_text = json.loads(response.text)
            print("===============================================================")
            print(response_text)
            print("===============================================================")
            return response_code, response_text
        except TimeoutError:
            print("Time out!")
            return None

    def post_origi(self):
        try:
            response = requests.request("POST", self.url, headers=self.headers, json=self.json,
                                        params=self.params, data=self.data, files=self.files)
            response_code = response.status_code
            response_text = response.text
            print("===============================================================")
            print(response_text)
            print("===============================================================")
            return response_code, response_text
        except TimeoutError:
            print("Time out!")
            return None
