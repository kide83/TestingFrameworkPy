import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value, timeout=10):
        """Clicks on an element after waiting for it to be clickable."""
        element = WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()

    def enter_text(self, locator_type, locator_value, text, timeout=10):
        """Finds an input field and enters text after waiting for it to be visible."""
        element = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located((locator_type, locator_value))
        )
        element.clear()
        element.send_keys(text)

    def select_dropdown_by_text(self, locator_type, locator_value, text, timeout=10):
        """Selects an option from a dropdown by visible text."""
        element = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located((locator_type, locator_value))
        )
        select = Select(element)
        select.select_by_visible_text(text)

    def get_element_text(self, locator_type, locator_value, timeout=10):
        """Gets the text of an element after waiting for it to be visible."""
        element = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located((locator_type, locator_value))
        )
        return element.text

    def take_screenshot(self, filename="screenshot.png"):
        """Captures a screenshot of the current page."""
        self.driver.save_screenshot(filename)
        logging.info(f"Screenshot saved as {filename}")
