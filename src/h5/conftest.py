import pytest
from selenium import webdriver

@pytest.fixture()
def wy_login():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def open_chrome():
    # 打开浏览器非调试模式
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",['enable-automation'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def env():
    """
    环境维护
    :return:
    """

    class ENV():
        def __init__(self):
            self.base_url = "api-gateway.guahao-test.com"
            self.test_h5_url =  "https://wy.guahao.com"
            self.base_headers = {
                "weiyi-version": "1.04",
                "content-type": "application/json; charset=utf-8",
                "weiyi-appid": "p_h5_weiyi",
                "weiyi-authtoken": ""
            }

    env = ENV()
    return env