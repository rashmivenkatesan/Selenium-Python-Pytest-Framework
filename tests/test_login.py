from pages.login_page import LoginPage


def test_login(setup):

    driver = setup

    driver.get("https://example.com")

    login = LoginPage(driver)

    login.enter_username("testuser")
    login.enter_password("password")
    login.click_login()

    assert driver.title == "Expected Title"
