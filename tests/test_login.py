import pytest

from pages.login_page import LoginPage
from utilities.json_reader import read_json


login_data = read_json("testdata/login_data.json")


@pytest.mark.parametrize("data", login_data)
def test_login(setup, data):

    driver = setup

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.enter_username(data["username"])
    login.enter_password(data["password"])
    login.click_login()

    if data["expected"] == "success":
        assert "inventory" in driver.current_url

    else:
        assert "Epic sadface" in driver.page_source
