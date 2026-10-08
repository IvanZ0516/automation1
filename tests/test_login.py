import time

from pages.login_page import LoginPage

def test_login_page(driver,base_url,credentials):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"],credentials["password"])
    #time.sleep(5)
    assert "wrong_url" in driver.current_url, "Login failed"
    #login.load()
    #login.login("standard_user","secret_sauce")

