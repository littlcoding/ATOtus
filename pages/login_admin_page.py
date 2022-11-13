from selenium.webdriver.common.by import By
from pages.Base_page import BasePage

class LoginAdminPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")

    def look_for_elements(self):
        self.element(self.USERNAME_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.FORGOT_PASSWORD)
        self.element(self.OPENCART_LINK)

    def login_admin(self, username, password):
        self._input(self.element(self.USERNAME_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self
