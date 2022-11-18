import time
import ddddocr


# 本用例用以后续浏览器验证码识别使用
class Test:
    def test_yq_login(self,open_chrome):
        driver = open_chrome
        driver.get("https://www.nbqy.gov.cn/itown-manage/login")
        time.sleep(1)
        # 下载验证码图片
        imgCode = driver.find_element_by_xpath("//img[@class='validate-code']")
        imgCode.screenshot("code.png")

        # 利用dddddocr识别验证码
        ocr = ddddocr.DdddOcr()
        with open("code.png","rb") as fp:
            image = fp.read()
        result = ocr.classification(image)
        # 仅打印无实际作用
        print("=======================================")
        print(result)

        driver.find_element_by_xpath("//input[@placeholder='输入用户名']").send_keys("18682970114")
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("zhyq@0114")
        # 输入验证码
        driver.find_element_by_xpath("//input[@placeholder='验证码']").send_keys(result)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='el-button login-button']").click()
        time.sleep(2)
        # 判断当前账号是否已登录过
        try:
            driver.find_element_by_xpath("//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]//span").click()
            print("当前账号已登录过")
        except:
            print("当前账号第一次登录")
        time.sleep(2)

        excepted = "周开发"
        actual = driver.find_element_by_xpath("//div[@class='welcome-info']").text
        print(actual)
        assert excepted == actual
