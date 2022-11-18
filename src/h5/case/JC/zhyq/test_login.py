import time
from selenium import webdriver

from src.h5.pages.zhyqlogin_page import ZhyqPage


class TestZhyq:
    def test_yq_login(self,open_chrome):
        driver = open_chrome
        zhyq_page = ZhyqPage(driver)
        zhyq_page.load()
        zhyq_page.login('18682970101','Zkf960114','1111')
        # 封装打开浏览器和查找元素操作后省略内容
        # driver.get("http://20.21.1.242:8081/ipark-manage/base/login")
        # time.sleep(1)
        # driver.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys("18682970101")
        # driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("Zkf960114")
        #
        time.sleep(2)
        excepted = "周开发园区"
        actual = driver.find_element_by_xpath("//span[@class='user-name']").text
        print(actual)
        # if actual == excepted:
        #    print('断言成功')
        # else:
        #     print('断言失败，请检查用例')
        assert excepted == actual

