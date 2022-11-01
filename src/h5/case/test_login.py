import time
import pytest

from selenium.webdriver.common.by import By

from src.h5.pages.login import LoginPage

class TestLogin:
    def test_login_success(self,wy_login):
        driver = wy_login
        login_page = LoginPage(driver)
        login_page.load()
        driver.find_element(By.XPATH,"//body//li[2]").click()
        login_page.login('18682970114','123456')
        time.sleep(2)

        #断言跳转地址
        time.sleep(0.5)
        assert driver.current_url == login_page.my
        print(driver.current_url)

    # def test_login_failed(self,wy_login):
    #     driver = wy_login
    #     login_page = LoginPage(driver)
    #     login_page.load()
    #     driver.find_element(By.CLASS_NAME,'user-top-nologin-btn').click()
    #     driver.find_element(By.XPATH,"//a[@class='s-btn phone-btn']").click()
    #     driver.find_element(By.XPATH,"//body//li[2]").click()
    #     login_page.login('18682970114','123456')
    #     time.sleep(2)
    #
    #     #断言跳转地址
    #     time.sleep(0.5)
    #     assert driver.current_url == login_page.my
    #     print(driver.current_url)





