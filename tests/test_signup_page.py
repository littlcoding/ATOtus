from pages.signup_page import SignupPage
from test_data.users import get_new_user


def test_main_page(browser):
    browser.get(browser.base_url + '/index.php?route=account/register')
    SignupPage(browser).look_for_elements()

def test_sign_up(browser):
    browser.get(browser.base_url)
    SignupPage(browser).go_to_sign_up().sign_up(*get_new_user())
