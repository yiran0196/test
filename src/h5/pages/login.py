from selenium.webdriver.common.by import By


class LoginPage:
    url = 'https://www.jkqd.org.cn/yuantu/h5-cli/2.29.93/login-phone.html?unionId=29&redirecturl=https%3A%2F%2Fwww.jkqd.org.cn%2Fyuantu%2Fh5-app%2Foutpatient%2F%23%2Fuser-center%3FunionId%3D29&spm=100.sign-in.1000.2'
    my = 'https://www.jkqd.org.cn/yuantu/h5-app/outpatient/#/user-center?unionId=29'
    cardlist = 'https://www.jkqd.org.cn/yuantu/h5-app/patient-card/#/card-list?unionId=29'

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element(By.XPATH,"//div[@class='login-phone login-new-wrap']//div[1]//div[1]//input[1]").send_keys(username)
        self.driver.find_element(By.XPATH,"//div[2]//div[1]//input[1]").send_keys(password)
        self.driver.find_element(By.XPATH,"//div[@class='login-button-wrap']//button").click()
        return self

    def load(self):
        self.driver.get(self.url)
        return self


    def clear(self):
        self.driver.find_element(By.XPATH,"//div[@class='login-phone login-new-wrap']//div[1]//div[1]//input[1]").clear()
        self.driver.find_element(By.XPATH,"//div[2]//div[1]//input[1]").clear()
        return self
