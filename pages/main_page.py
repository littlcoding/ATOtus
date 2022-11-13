from selenium.webdriver.common.by import By
from pages.Base_page import BasePage

class MainPage(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse')
    CAROUSEL = (By.CSS_SELECTOR, '#carousel0.swiper-container')
    FEATURED_STUFF = (By.CSS_SELECTOR, '.product-layout')
    MY_ACCOUNT = (By.XPATH, "//*[@title='My Account']")
    HEADER = (By.CSS_SELECTOR, '#logo .img-responsive')
