from pages.login_admin_page import LoginAdminPage
from pages.admin_page import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

product_name = 'random_name'

@allure.feature('Admin')
@allure.story('Testing items')
@allure.title('Add new item by Admin')
def test_add_item(browser):
    browser.get(browser.base_url + '/admin')
    LoginAdminPage(browser).login_admin('user', 'bitnami')
    AdminPage(browser).select_left_menu('catalog', 'Products')
    AdminPage(browser).add_new_item()
    AdminPage(browser).fill_general_tab(product_name=product_name, tag='random_tag')
    AdminPage(browser).pick_tab(tab_name='Data')
    AdminPage(browser).fill_model_tab(model='random_model')
    AdminPage(browser).add_new_item()

@allure.feature('Admin')
@allure.story('Testing items')
@allure.title('Delete item by Admin')
def test_delete_item(browser):
    browser.get(browser.base_url + '/admin')
    LoginAdminPage(browser).login_admin('user', 'bitnami')
    AdminPage(browser).select_left_menu('catalog', 'Products')
    AdminPage(browser).delete_item(product_name=product_name)
    alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
    alert.accept()


