import pytest
from pages.search_page import SearchPage
from utils.test_data import SEARCH_TERMS

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://example.com")  # Replace with actual URL
    yield driver
    driver.quit()

@pytest.mark.parametrize("search_term", SEARCH_TERMS)
def test_search_product(driver, search_term):
    search_page = SearchPage(driver)

    search_page.enter_search_term(search_term)
    search_page.click_search_button()

    assert search_page.is_product_list_displayed()
