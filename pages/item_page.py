from selenium.webdriver.common.by import By
from .base_page import BasePage

class ItemPage(BasePage):
    ITEM_DETAILS = (By.XPATH,'//div[@class="inventory_details_container"]')
    ITEM_NAME = (By.XPATH,'//div[@class="inventory_details_name large_size"]')
    ADD_TO_CART_BTN = (By.ID,'add-to-cart')

    def item_details_load(self):
        return self.is_visible(self.ITEM_DETAILS)

    def get_item_name(self):
        return self.text_of(self.ITEM_NAME)
