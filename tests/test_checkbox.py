from utils.functions import BrowserManager

def test_checkbox():

    browser = BrowserManager("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/checkboxes")

    browser.select_checkbox("//form[@id='checkboxes']/input[1]", "xpath")

    browser.take_screenshot("checkbox_screenshot")

    browser.close_browser()