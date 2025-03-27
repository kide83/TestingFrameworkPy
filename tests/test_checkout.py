import pytest
from pages.checkout_page import CheckoutPage
from utils.test_data import CHECKOUT_DETAILS

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://example.com/checkout")  # Replace with actual URL
    yield driver
    driver.quit()

def test_checkout_process(driver):
    checkout_page = CheckoutPage(driver)

    checkout_page.add_item_to_cart()
    checkout_page.proceed_to_checkout()

    # Using test data from test_data.py
    checkout_page.fill_checkout_details(
        CHECKOUT_DETAILS["first_name"],
        CHECKOUT_DETAILS["last_name"],
        CHECKOUT_DETAILS["zip_code"]
    )

    checkout_page.place_order()

    assert "Order Confirmation" in driver.title  # Example assertion
