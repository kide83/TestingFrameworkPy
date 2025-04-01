from utils.functions import BrowserManager
from utils.test_data import TEST_USERS

def test_valid_login():
    browser = BrowserManager("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/login")

    browser.enter_text("username", "id", "tomsmith")

    browser.enter_text("password", "id", "SuperSecretPassword!")

    browser.click_button("//*[@id='login']/button", "xpath")

    browser.take_screenshot("loggedin_area_screenshot")

    assert "secure area" in browser.get_element_text("flash-messages", "id")  # Example assertion

    browser.click_button("//*[@id='content']/div/a", "xpath")

    browser.take_screenshot("loggedout_area_screenshot")

    browser.close_browser()




    # Using the first test user from test_data.py
    #username = TEST_USERS[0]["username"]
    #password = TEST_USERS[0]["password"]






