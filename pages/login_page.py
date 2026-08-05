from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import get_logger


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def enter_username(self, username):

        self.logger.info("Entering username")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self, password):

        self.logger.info("Entering password")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(password)

    def click_login(self):

        self.logger.info("Clicking login button")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
