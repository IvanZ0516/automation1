import time

from pages.login_page import LoginPage

def test_login_page(driver,base_url,credentials):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"],credentials["password"])
    #time.sleep(5)
    #login.load()
    #login.login("standard_user","secret_sauce")

def test_login_page_incorrect_pwd(driver,base_url,wrong_password):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(wrong_password["username"],wrong_password["wrong_password"])
    assert login.wait_element(),True


