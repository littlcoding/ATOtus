from pages.login_admin_page import LoginAdminPage

def test_add_item(browser):
    browser.get(browser.base_url + '/admin')
    LoginAdminPage(browser).look_for_elements()
