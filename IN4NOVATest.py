from selenium import webdriver

def test_open_in4nova():
    driver = webdriver.Chrome()
    driver.get("https://www.in4nova.com")
    assert "IN4NOVA" in driver.title
    driver.quit()

# Testing Again
