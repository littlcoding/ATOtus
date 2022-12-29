from pages.login_admin_page import LoginAdminPage
import allure


@allure.feature('Regression')
@allure.title('Smoke login admin page')
def test_login_admin(browser):
    browser.get(browser.base_url + '/admin')
    LoginAdminPage(browser).look_for_elements()
