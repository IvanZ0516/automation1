from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    HEADER = (By.XPATH, '//div[text()="Swag Labs"]')
    PRODUCTS_LIST = (By.XPATH, '//div[@class="inventory_list"]')
    FILTERS = (By.XPATH, '//select[@class="product_sort_container"]')
    ITEM = (By.CLASS_NAME, 'inventory_item_name ')

    def inventory_page_load(self):
        return self.is_visible(self.PRODUCTS_LIST)

    def get_title(self):
        return self.text_of(self.HEADER)

    def click_item(self):
        self.is_visible(self.ITEM)
        self.click(self.ITEM)