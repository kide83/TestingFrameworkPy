import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.selenium_helpers import SeleniumHelper  # Import custom library


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    helper = SeleniumHelper(driver)  # Create an instance of the helper class

    driver.get("https://practicetestautomation.com/practice-test-login/")

    helper.enter_text(By.ID, "username", "student")
    helper.enter_text(By.ID, "password", "Password123")
    helper.click_element(By.ID, "submit")

    # Verify login was successful
    success_message = helper.get_element_text(By.TAG_NAME, "h1")
    assert success_message == "Logged In Successfully", "Login failed!"
