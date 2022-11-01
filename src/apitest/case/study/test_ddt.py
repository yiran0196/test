from src.apitest.common.requesthandler import RequestHandler
import pytest


datas = [
    {"method": "post" ,
         "url": "http://api.lemonban.com/futureloan/member/register",
     "req_data": {"mobile_phone": "18610100022","pwd": "123456789","reg_name": "py37小简"}},
    {"method": "post",
     "url": "http://api.lemonban.com/futureloan/member/login",
     "req_data":{"mobile_phone": "18610100022","pwd": "123456789"}},
    {"method": "post",
     "url": "http://api.lemonban.com/futureloan/member/recharge",
     "req_data": {"member_id": None,"amount": 1000}}
]


mr = RequestHandler()

# 一组就是一条用例
# 某一组即便运行失败了，下一组仍然会运行。
@pytest.mark.parametrize("item", datas)
def test_api1(item):
    resp = mr.visit(item["method"], item["url"], item["req_data"])
    print(resp.json())
    assert False


# def test_api1():
#     for item in datas:
#         resp = mr.send_requests(item["method"], item["url"], item["req_data"])
#         print(resp.json())
#         assert False



# def test_ap2():
#     resp = mr.send_requests(datas[1]["method"], datas[1]["url"], datas[1]["req_data"])
#     print(resp.json())
#
# def test_api3():
#     resp = mr.send_requests(datas[2]["method"], datas[2]["url"], datas[2]["req_data"])
#     print(resp.json())