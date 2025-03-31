from utils.functions import BrowserManager

def test_dropdown_contains_option():

    browser = BrowserManager("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/dropdown")

    browser.check_dropdown_list_item("dropdown", "id","Option 2")

    browser.click_dropdown_list_item("dropdown", "id","Option 1")

    browser.take_screenshot("drop_down_item_screenshot")

    browser.close_browser()
