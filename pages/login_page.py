from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID,'user-name')
    PASSWORD = (By.ID,'password')
    LOGIN_BTN = (By.ID,'login-button')
    ERROR_LOGIN = (By.XPATH,'//h3[@data-test="error"]')

    def load(self, base_url):
        self.open(base_url)

    def login(self,username,password):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)

    def wait_element(self):
        return self.is_visible(self.ERROR_LOGIN)

