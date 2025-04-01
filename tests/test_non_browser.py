from utils.functions import OtherFunctions

def test_non_browser():

    functions = OtherFunctions()

    new_vorschrift_number = functions.generate_random_vorschrift_number()
    print(new_vorschrift_number)