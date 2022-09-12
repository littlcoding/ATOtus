from selenium.webdriver.common.by import By

class SignupPage:
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    TEL_NO_INPUT = (By.ID, "input-telephone")
    PASS_INPUT = (By.ID, 'input-password')
