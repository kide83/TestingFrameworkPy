import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")  # Replace with actual URL
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()

    assert "Dashboard" in driver.title  # Example assertion
