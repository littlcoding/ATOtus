from pages.signup_page import SignupPage
from test_data.users import get_new_user
import allure


@allure.feature('Regression')
@allure.title('Smoke register page')
def test_register_page(browser):
    browser.get(browser.base_url + '/index.php?route=account/register')
    SignupPage(browser).look_for_elements()

@allure.feature('Regression')
@allure.title('Smoke signup page')
def test_sign_up(browser):
    browser.get(browser.base_url)
    SignupPage(browser).go_to_sign_up().sign_up(*get_new_user())
