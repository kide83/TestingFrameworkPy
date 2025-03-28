from utils.functions import BrowserManager

def test_dropdown_contains_option():

    browser = BrowserManager("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/dropdown")


    dropdown = browser.get_dropdown_list()
    options = [option.text for option in dropdown.options]
    dropdown.click()

    expected_option = "Option 2"  # Change this based on what you expect
    assert expected_option in options, f"'{expected_option}' not found in dropdown options"

    browser.close_browser()
