import pytest
from selenium import webdriver
from utils.logger import get_logger

logger = get_logger()

@pytest.fixture
def driver():
    logger.info("Starting WebDriver")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    logger.info("Closing WebDriver")
    driver.quit()
