from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "search")
        self.search_button = (By.ID, "searchBtn")
        self.product_list = (By.CLASS_NAME, "product-list")

    def enter_search_term(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def is_product_list_displayed(self):
        return len(self.driver.find_elements(*self.product_list)) > 0
