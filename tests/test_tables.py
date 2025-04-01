from utils.functions import BrowserFunctions

def test_tables():

    browser = BrowserFunctions("Chrome")

    browser.open_url("https://the-internet.herokuapp.com/tables")

    # browser.take_screenshot("table_screenshot")

    # assert "http://www.jsmith.com" in browser.get_table_cell_value("table1", 1, 5)




    # Clicks "Edit" button in second row... treba doraditi za klliktanje na link u polju, i ako nema id taga npr...
    # browser.click_button_in_table_cell("users-table", 1, "edit-btn")

    # Check if data is found in table - RADI, proverio
    # if browser.is_value_found_in_table("table1", "Conway"):
    #     print("Data found in the table!")

    # Get column number from table
    # column_number  = browser.get_column_number("table1", "Action")
    # print(f"'Action' column is at position: {column_number}")

    # Get number of rows in table
    row_count = browser.get_rows_count("table1")
    print(f"Number of rows: {row_count}")






    browser.close_browser()
