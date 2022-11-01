import ddt
import requests
import pytest

class MyRequest:
    def __init__(self):
        self.headers ={"Content-Type":"application/javascript;charset=UTF-8"}
    # 方法一
    # def send_request(self,url,method,json=None,params=None):
    #     #调用requests的方法发起一个请求，并获得响应结果
    #     resp = requests.request(method,url,json=json,params=params,headers=self.headers)
    # 方法二
    @pytest.mark.parametrize("命名",数组名)
    def send_request(self,url,method,data):
        if method.upper() == "GET":
            resp = requests.request(method,url,json=data,headers=self.headers)
        else:
            resp = requests.request(method, url, params=data, headers=self.headers)
        pass
    pass