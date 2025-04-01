from utils.functions import BrowserManager

def test_tables():

    browser = BrowserManager("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/tables")

    browser.take_screenshot("table_screenshot")

    assert "http://www.jsmith.com" in browser.get_table_cell_value("table1", 1, 5)

    browser.close_browser()