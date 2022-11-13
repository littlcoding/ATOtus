from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LOGIN_DROPDOWN = (By.XPATH, "//*[@title='My Account']")
    LOGIN = (By.XPATH, "//*[text()='Login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")
    HOME_PAGE_BUTTON = (By.CSS_SELECTOR, '.img-responsive')

    def __init__(self, browser):
        self.browser = browser

    def click(self, element):
        ActionChains(self.browser).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def login(self, username, password):
        self.click(self.element(self.LOGIN_DROPDOWN))
        self.click(self.element(self.LOGIN))
        self._input(self.element(self.EMAIL_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def return_to_home_page(self):
        self.click(self.element(self.HOME_PAGE_BUTTON))

