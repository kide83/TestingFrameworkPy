from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger()

class BrowserManager:
    def __init__(self, browser_name="Chrome"):
        options = Options()
        options.add_argument("--headless")  # Run in headless mode (no UI)
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

    def get_dropdown_list(self):
        return self.driver.find_element(By.ID, "dropdown")


