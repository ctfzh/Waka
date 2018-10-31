# -*- coding: UTF-8 -*-

import unittest
from common.configHttp import ConfigHttp
import readConfig


class UserTest(unittest.TestCase):
    # setUp用于初始化工作,
    def setUp(self):
        config = readConfig.ReadConfig()
        self.url = config.get_http("test_url")
        self.header = {
            "deviceType": "h5",
            "t": "1540804675678000",
            "proId": "frwl9f50d6ecb69ca8bd8899b5dc6ae19df8",
            "module": "wk-port",
            "requestSourceIp": "114.251.159.68",
            "version": "1.1",
            "token": "token"
        }

    # 4.获取短信验证码接口
    def test_sendH5(self):
        path = "/wkStRoute/api/sms/sendH5"
        post_parm = {"phoneNo": "18610660297", "validate": "001897f346018a61da3a46034203f6e9"}
        response = ConfigHttp()
        response.set_url(self.url+path)
        response.set_headers(self.header)
        response.set_data(post_parm)
        print(self.url+path)
        results = ConfigHttp.post_origi(response)
        # assert results[0] == 200
        # assert results[1]["sts"] == "000000"
        # assert results[1]["msg"] == "成功"


if __name__ == '__main__':
    unittest.main()


