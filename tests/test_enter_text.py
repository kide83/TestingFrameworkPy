from utils.functions import BrowserManager

def test_enter_text():

    browser = BrowserManager("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/inputs")

    browser.click_element("//*[@id='content']/div/div/div/input", "xpath")

    browser.enter_text("//*[@id='content']/div/div/div/input", "xpath", 76)

    browser.take_screenshot("input_field_screenshot")

    browser.close_browser()


