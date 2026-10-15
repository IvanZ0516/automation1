import time

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.item_page import ItemPage

def test_inventory_page_load(driver, base_url, credentials):
    inventory_page = InventoryPage(driver)
    login_page = LoginPage(driver)
    item_page = ItemPage(driver)
    login_page.load(base_url)
    login_page.login(credentials["username"], credentials["password"])
    #time.sleep(5)
    assert inventory_page.get_title(), True
    assert inventory_page.inventory_page_load(), True
    inventory_page.click_item()
    assert item_page.item_details_load(), True
    #time.sleep(5)


