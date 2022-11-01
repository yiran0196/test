import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
"""
def test_tb():
    # os.popen("sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222")
    # time.sleep(3)

    options = webdriver.ChromeOptions()
    # options.debugger_address = '127.0.0.1:9222'
    # 调用浏览器非自动测试软件的控制
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://login.taobao.com/member/login.jhtml')
    time.sleep(1)
    # driver.find_element_by_link_text('使用其他帐户登录')
    driver.find_element_by_id('fm-login-id').send_keys('18682970114')
    driver.find_element_by_id('fm-login-password').send_keys('Mzhou0196')
    # driver.find_element_by_class_name("fm-button fm-submit ").click()
    driver.find_element_by_xpath("//button[@class='fm-button fm-submit password-login']").click()
    time.sleep(2)
    excepted = '卖家打电话就差评！'
    actual = driver.find_element_by_xpath("//div[@class='s-name']//em[1]")
    print(actual.text)
    assert actual.text == excepted