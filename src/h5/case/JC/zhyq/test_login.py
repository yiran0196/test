import time
from selenium import webdriver
class TestZhyq:
    def test_yq_login(self,open_chrome):
        driver = open_chrome
        driver.get("http://20.21.1.242:8081/ipark-manage/base/login")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys("18682970101")
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("Zkf960114")
        driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("1111")
        driver.find_element_by_xpath("//div[@class='el-form-item__content']//button[@class='el-button el-button--default']//span").click()
        time.sleep(2)
        excepted = "周开发园区"
        actual = driver.find_element_by_xpath("//span[@class='user-name']").text
        print(actual)
        assert actual == excepted