from pages.one_product_page import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url + '/smartphone/iphone')
    ProductPage(browser).look_for_elements()
