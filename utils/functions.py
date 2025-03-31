from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from selenium.webdriver.support.ui import Select
import os
import time

logger = get_logger()

class BrowserManager:
    def __init__(self, browser_name="Chrome"):
        options = Options()
        #options.add_argument("--headless")  # Run in headless mode (no UI)
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # Prevent /dev/shm issues
        options.add_argument("--user-data-dir=/tmp/chrome-user-data")  # Set a unique user data directory

        """Initialize the browser based on the given name."""
        if browser_name.lower() == "chrome":
            logger.info("Starting Chrome WebDriver")
            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        elif browser_name.lower() == "edge":
            logger.info("Starting Edge WebDriver")
            self.driver = webdriver.Edge(options=options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    def open_url(self, url):
        """Open a URL in the selected browser."""
        self.driver.get(url)

    def close_browser(self):
        """Close the browser instance."""
        logger.info("Closing WebDriver")
        self.driver.quit()

    def get_page_title(self):
        """Get the title of the current page."""
        return self.driver.title

    def check_dropdown_list_item(self, locator, locator_type, item_value):
        if locator_type.lower() == "id":
            dropdown_element = self.driver.find_element(By.ID, locator)
        elif locator_type.lower() == "xpath":
            dropdown_element = self.driver.find_element(By.XPATH, locator)
        else:
            raise ValueError("Invalid locator type! Use 'id' or 'xpath'.")
        dropdown = Select(dropdown_element)
        options = [option.text for option in dropdown.options]
        expected_option = item_value
        assert expected_option in options, f"'{expected_option}' not found in dropdown options"

    def click_dropdown_list_item(self, locator, locator_type, item_value):
        if locator_type.lower() == "id":
            dropdown_element = self.driver.find_element(By.ID, locator)
        elif locator_type.lower() == "xpath":
            dropdown_element = self.driver.find_element(By.XPATH, locator)
        else:
            raise ValueError("Invalid locator type! Use 'id' or 'xpath'.")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(item_value)
        selected_option = dropdown.first_selected_option.text
        assert selected_option == item_value, f"Expected '{item_value}', but got '{selected_option}'"

    def click_element(self, locator, locator_type):
        if locator_type.lower() == "id":
            element = self.driver.find_element(By.ID, locator)
        elif locator_type.lower() == "xpath":
            element = self.driver.find_element(By.XPATH, locator)
        else:
            raise ValueError("Invalid locator type! Use 'id' or 'xpath'.")
        element.click()

    def get_element_text(self, locator, locator_type):
        if locator_type.lower() == "id":
            element = self.driver.find_element(By.ID, locator)
        elif locator_type.lower() == "xpath":
            element = self.driver.find_element(By.XPATH, locator)
        else:
            raise ValueError("Invalid locator type! Use 'id' or 'xpath'.")
        return element.text

    def take_screenshot(self, filename):
        """Captures a screenshot of the current page."""
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshots/{filename}_{timestamp}.png"

        os.makedirs("screenshots", exist_ok=True)

        self.driver.save_screenshot(screenshot_name)
        logger.info(f"Screenshot saved as {filename}")

    def enter_text(self, locator, locator_type, text):
        if locator_type.lower() == "id":
            element = self.driver.find_element(By.ID, locator)
        elif locator_type.lower() == "xpath":
            element = self.driver.find_element(By.XPATH, locator)
        else:
            raise ValueError("Invalid locator type! Use 'id' or 'xpath'.")
        element.clear()
        element.send_keys(text)

