import time
from selenium.webdriver.common.by import By
from src.h5.case.test_login import TestLogin
from src.h5.pages.login import LoginPage


class TestMy:
    def test_my(self,open_chrome):
        driver = open_chrome
        login_page = LoginPage(driver)
        time.sleep(1)
        login_page.load()
        driver.find_element(By.XPATH,"//body//li[2]").click()
        login_page.login('18682970114','123456')
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[@class='user-applycard-login']//div[1]//div[1]//div[2]").click()

        assert driver.current_url == login_page.cardlist