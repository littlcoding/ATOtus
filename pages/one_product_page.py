from selenium.webdriver.common.by import By

class ProductPage:
    PRODUCT_IMG = (By.CSS_SELECTOR, '.thumbnails > li:first-child')
    ADDITIONAL_PRODUCT_IMG = (By.CSS_SELECTOR, '.image-additional')
    DESCRIPTION_TABS = (By.XPATH, "//*[@data-toggle='tab']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#product #button-cart')
    RELATED_PRODUCTS = (By.CSS_SELECTOR, '.col-xs-6.col-sm-3')

    def look_for_elements(self):
        self.element(self.PRODUCT_IMG)
        self.element(self.ADDITIONAL_PRODUCT_IMG)
        self.element(self.DESCRIPTION_TABS)
        self.element(self.ADD_TO_CART_BUTTON)
        self.element(self.RELATED_PRODUCTS)
