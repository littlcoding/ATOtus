from pages.one_product_page import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url + '/smartphone/iphone')
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(ProductPage.ADDITIONAL_PRODUCT_IMG))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(ProductPage.RELATED_PRODUCTS))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(ProductPage.DESCRIPTION_TABS))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ProductPage.PRODUCT_IMG))
