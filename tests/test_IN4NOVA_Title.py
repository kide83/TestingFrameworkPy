from utils.functions import BrowserManager


def test_open_in4nova():

    browser = BrowserManager("Chrome")

    browser.open_url("https://www.in4nova.com")

    assert "IN4NOVA" in browser.get_page_title()

    browser.close_browser()
