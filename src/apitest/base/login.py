import pytest
from src.apitest.common.requesthandler import RequestHandler


class Login:
    def login(self):
        url = 'https://api-qdjh.jkqd.org.cn/user-web/restapi/common/ytUsers/login'
        params = {
            "password": "14e1b600b1fd579f47433b88e8d85291",
            "phoneNum": "18682970114",
            "unionId": "29"
        }
        req = RequestHandler()
        resp = req.visit("get", url, params)
        # 获取当前登录接口的cookies
        cookies = resp.cookies
        return cookies

