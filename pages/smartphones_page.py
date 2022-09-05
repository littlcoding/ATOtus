from selenium.webdriver.common.by import By

class SmartphonesPage:
    CATEGORIES_LIST = (By.CSS_SELECTOR, '.list-group')
    PRODUCTS = (By.CSS_SELECTOR, '.product-layout')
    SORT_DROPDOWN = (By.ID, 'input-sort')
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[text()='Add to Cart']")
    PAGES_COUNTER = (By.CSS_SELECTOR, '.col-sm-6.text-right')
