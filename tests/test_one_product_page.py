from pages.one_product_page import ProductPage
import allure


@allure.feature('Regression')
@allure.title('Smoke item page')
def test_iphone_page(browser):
    browser.get(browser.base_url + '/smartphone/iphone')
    ProductPage(browser).look_for_elements()
