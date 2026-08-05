from pages.login_page import LoginPage
from utilities.json_reader import read_json


def test_login(setup):

    driver = setup

    login_data = read_json("testdata/login_data.json")

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.enter_username(login_data["username"])
    login.enter_password(login_data["password"])
    login.click_login()

    assert "inventory" in driver.current_url
