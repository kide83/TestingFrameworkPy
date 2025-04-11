from utils.functions import OtherFunctions

def test_non_browser():

    functions = OtherFunctions()

    #new_vorschrift_number = functions.generate_random_vorschrift_number()
    #print(new_vorschrift_number)

    #new_arbeitskreiss_number = functions.generate_random_arbeitskreiss_number()
    #print(new_arbeitskreiss_number)

    # row_index = 2 je prvi red, red 1 je headers
    #value = functions.get_value_from_excel(r"C:\TestingFrameworkPy\testdata\test_data.xlsx", "Regulations", "Name", 2)
    #print(f"Value from Excel: {value}")

    # Write to Excel Sheet
    #functions.write_to_excel(r"C:\TestingFrameworkPy\testdata\test_data.xlsx", "Regulations", "Name", 2, "Test123")

    # Read PDF file
    assert functions.is_text_in_pdf(
        "C:/TestingFrameworkPy/testdata/DejanMirkovic.pdf",
        "UGOVOR O RADU"
    ), "UGOVOR O RADU was not found in pdf file."






