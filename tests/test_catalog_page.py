from pages.smartphones_page import SmartphonesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url + '/smartphone')
    SmartphonesPage(browser).look_for_elements()
