from utils.functions import BrowserFunctions

def test_dropdown_contains_option():

    browser = BrowserFunctions("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/dropdown")

    browser.check_dropdown_list_item("dropdown", "id","Option 2")

    browser.click_dropdown_list_item("dropdown", "id","Option 1")

    browser.take_screenshot("drop_down_item_screenshot")

    browser.click_random_dropdown_list_item("dropdown", "id")

    browser.take_screenshot("drop_down_random_item_screenshot")

    browser.close_browser()
