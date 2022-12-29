from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
import allure

class SignupPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    TEL_NO_INPUT = (By.ID, "input-telephone")
    PASS_INPUT = (By.ID, 'input-password')
    PASS_CONFIRM = (By.ID, 'input-confirm')
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='content']")
    MY_ACCOUNT = (By.XPATH, "//*[@title='My Account']")
    REGISTER_LINK = (By.LINK_TEXT, 'Register')

    @allure.step('Smoke check for elements')
    def look_for_elements(self):
        self.element(self.FIRST_NAME_INPUT)
        self.element(self.LAST_NAME_INPUT)
        self.element(self.EMAIL_INPUT)
        self.element(self.TEL_NO_INPUT)
        self.element(self.PASS_INPUT)

    @allure.step('Going to signup page')
    def go_to_sign_up(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.REGISTER_LINK))
        return self

    @allure.step('Signing in the new user')
    def sign_up(self, firstname, lastname, email, telephone, password, passwordconfirm):
        self._input(self.element(self.FIRST_NAME_INPUT), firstname)
        self._input(self.element(self.LAST_NAME_INPUT), lastname)
        self._input(self.element(self.EMAIL_INPUT), email)
        self._input(self.element(self.TEL_NO_INPUT), telephone)
        self._input(self.element(self.PASS_INPUT), password)
        self._input(self.element(self.PASS_CONFIRM), passwordconfirm)
        self.click(self.element(self.CONTINUE_BUTTON))
        return self
