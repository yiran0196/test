import pytest
import requests

from src.apitest.base.login import Login
from src.apitest.common.dbhandler import DBHandler
from src.apitest.common.loghandler import logger
from src.apitest.common.requesthandler import RequestHandler

# 创建session会话管理
# session = requests.session()
# print(session)

class Test_My(Login):
        def test_my(self):
            cookies = Login.login(self)
            url = 'https://api-qdjh.jkqd.org.cn/user-web/restapi/reservation/getRegPagesByStatus'
            params = {"unionId" : "29",
                     "corpId" : "34605",
                     "patientId" : "15948214"
                     }
            req = RequestHandler()
            resp = req.visit("get",url,params,cookies = cookies)
            assert resp.status_code == 200
            print(resp.status_code)

        def test_my2(self):
            cookies = Login.login(self)
            url = 'https://api-qdjh.jkqd.org.cn/user-web/restapi/reservation/getRegPagesByStatus'
            params = {"unionId" : "29",
                     "corpId" : "34605",
                     "patientId" : "15948214"
                     }
            req = RequestHandler()
            resp = req.visit("get",url,params,cookies = cookies)
            logger.info('')
            assert resp.status_code == 200
            print(resp.status_code)


if __name__ == '__main__':
    pytest.main()
