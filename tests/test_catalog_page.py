from pages.smartphones_page import SmartphonesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url + '/smartphone')
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(SmartphonesPage.ADD_TO_CART_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SmartphonesPage.PAGES_COUNTER))
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(SmartphonesPage.PRODUCTS))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(SmartphonesPage.SORT_DROPDOWN))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(SmartphonesPage.CATEGORIES_LIST))
