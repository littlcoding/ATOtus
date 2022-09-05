from pages.signup_page import SignupPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url + '/index.php?route=account/register')
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.FIRST_NAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.LAST_NAME_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.EMAIL_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.TEL_NO_INPUT))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SignupPage.PASS_INPUT))
