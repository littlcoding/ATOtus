from pages.elements.Currency import CurrencyElement
import allure


@allure.feature('Regression')
@allure.title('Smoke currency page')
def test_currency_choise(browser):
    browser.get(browser.base_url)
    CurrencyElement(browser).change_currensy()
