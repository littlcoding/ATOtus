from pages.smartphones_page import SmartphonesPage
import allure

@allure.feature('Regression')
@allure.title('Smoke item page')
def test_main_page(browser):
    browser.get(browser.base_url + '/smartphone')
    SmartphonesPage(browser).look_for_elements()
