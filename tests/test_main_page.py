from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url)
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(MainPage.CART_BUTTON))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.MY_ACCOUNT))
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(MainPage.FEATURED_STUFF))
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable(MainPage.MY_ACCOUNT))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(MainPage.HEADER))
