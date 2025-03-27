from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, "addToCart")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.zip_code_input = (By.ID, "zipCode")
        self.place_order_button = (By.ID, "placeOrder")

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def fill_checkout_details(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()
