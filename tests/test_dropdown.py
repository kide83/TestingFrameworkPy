import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_dropdown_contains_option(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")  # Example website

    dropdown = Select(driver.find_element(By.ID, "dropdown"))  # Find the dropdown
    options = [option.text for option in dropdown.options]  # Get all options as text

    expected_option = "Option 2"  # Change this based on what you expect
    assert expected_option in options, f"'{expected_option}' not found in dropdown options"



# Click on Drop Down list Item
# dropdown = driver.find_element(By.ID, "dropdown")
# dropdown.click()  # Click to open dropdown

# option = driver.find_element(By.XPATH, "//option[text()='Option 2']")  # Find specific option
# option.click()  # Click to select it



