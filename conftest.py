import os
import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )
            driver.save_screenshot(screenshot_path)
