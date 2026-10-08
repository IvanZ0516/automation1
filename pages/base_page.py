from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def open(self,url: str):
        self.driver.get(url)

    def find(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self,locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def type(self,locator,text: str):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def text_of(self,locator) -> str: #WILL EXTRACT A TEXT FROM AN ELEMENT
        return self.find(locator).text.strip() #STRIP REMOVES ALL WHITE SPACES AT THE BEGINNING OR AT THE END

    def is_visible(self,locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

