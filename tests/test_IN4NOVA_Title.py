from utils.functions import BrowserFunctions

def test_open_in4nova():

    browser = BrowserFunctions("Chrome")

    browser.open_url("https://www.in4nova.com")

    assert "IN4NOVA" in browser.get_page_title()

    browser.close_browser()
