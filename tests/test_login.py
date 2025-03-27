import pytest
from pages.login_page import LoginPage
from utils.test_data import TEST_USERS


@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")  # Replace with actual URL
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Using the first test user from test_data.py
    username = TEST_USERS[0]["username"]
    password = TEST_USERS[0]["password"]

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    assert "Dashboard" in driver.title  # Example assertion
