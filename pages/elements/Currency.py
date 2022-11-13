from selenium.webdriver.common.by import By
from pages.Base_page import BasePage


class CurrencyElement(BasePage):
    CURRENCY_CHOISE = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    CURRENCY_LIST = (By.XPATH, "//*[@class='currency-select btn btn-link btn-block']")

    def change_currensy(self):
        self.click(self.element(self.CURRENCY_CHOISE))
        self.click(self.element(self.CURRENCY_LIST))
