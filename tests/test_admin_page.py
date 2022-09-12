from pages.login_admin_page import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_inputs(browser):
    browser.get(browser.base_url + '/admin')
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    return WebDriverWait(browser, 2).until(EC.visibility_of_element_located(LoginAdminPage.USERNAME_INPUT))

def test_login_button(browser):
    browser.get(browser.base_url + '/admin')
    return WebDriverWait(browser, 2).until(EC.element_to_be_clickable(LoginAdminPage.LOGIN_BUTTON))

def test_forgot_pass(browser):
    browser.get(browser.base_url + '/admin')
    return WebDriverWait(browser, 2).until(EC.element_to_be_clickable(LoginAdminPage.FORGOT_PASSWORD))

def test_oc_link(browser):
    browser.get(browser.base_url + '/admin')
    return WebDriverWait(browser, 2).until(EC.element_to_be_clickable(LoginAdminPage.OPENCART_LINK))

