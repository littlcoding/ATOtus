from selenium.webdriver.common.by import By

class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
