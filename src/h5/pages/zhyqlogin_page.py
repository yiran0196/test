from selenium.webdriver.common.by import By


class ZhyqPage:
    url = 'http://20.21.1.242:8081/ipark-manage/base/login'
    def __init__(self,driver):
       self.driver = driver

    def login(self,username,password,code):
        self.driver.find_element(By.XPATH,"//input[@placeholder='请输入用户名']").send_keys(username)
        self.driver.find_element(By.XPATH,"//input[@placeholder='请输入密码']").send_keys(password)
        self.driver.find_element(By.XPATH,"//input[@placeholder='请输入验证码']").send_keys(code)
        self.driver.find_element(By.XPATH,"//div[@class='el-form-item__content']//button[@class='el-button el-button--default']//span").click()
    def load(self):
        self.driver.get(self.url)
        return self
    def clear(self):
        self.find_element(By.XPATH,"//input[@placeholder='请输入用户名']").clear()
        self.find_element(By.XPATH,"//input[@placeholder='请输入密码']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']").clear()
        return self