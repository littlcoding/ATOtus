from pages.main_page import MainPage

def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.login(username='qwe@gmail.com', password='qwer1234')
    main_page.return_to_home_page()
    main_page.element(locator=(MainPage.CART_BUTTON))
    main_page.element(locator=(MainPage.MY_ACCOUNT))
    main_page.element(locator=(MainPage.FEATURED_STUFF))
    main_page.element(locator=(MainPage.MY_ACCOUNT))
    main_page.element(locator=(MainPage.HEADER))
