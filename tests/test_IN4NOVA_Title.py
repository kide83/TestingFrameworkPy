from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_in4nova():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Prevent /dev/shm issues
    options.add_argument("--user-data-dir=/tmp/chrome-user-data")  # Set a unique user data directory

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.in4nova.com")
    assert "IN4NOVA" in driver.title
    driver.quit()
