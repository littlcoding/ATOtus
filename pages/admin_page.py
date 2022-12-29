from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
import allure


class AdminPage(BasePage):
    ADD_ITEM = (By.CSS_SELECTOR, '.pull-right .btn.btn-primary')
    DELETE_ITEM = (By.CSS_SELECTOR, '.pull-right .btn.btn-danger')
    NAME_FIELD = (By.NAME, 'product_description[1][name]')
    TAG_FIELD = (By.NAME, 'product_description[1][meta_title]')
    MODEL_FIELD = (By.ID, 'input-model')

    @allure.step('Select "{child_menu}" in the left toolbar')
    def select_left_menu(self, parent_menu, child_menu):
        menu = (By.ID, f'menu-{parent_menu}')
        sub_menu = (By.XPATH, f"//*[text()='{child_menu}']")
        self.click(self.element(menu))
        self.click(self.element(sub_menu))

    @allure.step('Click on Add new item button')
    def add_new_item(self):
        self.click(self.element(self.ADD_ITEM))

    @allure.step('Filling product name and tag with "{product_name}" "{tag}"')
    def fill_general_tab(self, product_name, tag):
        self._input(self.element(self.NAME_FIELD), product_name)
        self._input(self.element(self.TAG_FIELD), tag)

    @allure.step('Select "{tab_name}" tab')
    def pick_tab(self, tab_name):
        tab = (By.XPATH, f"//*[contains(@class, 'nav nav-tabs')]/li//*[contains(text(), '{tab_name}')]")
        self.click(self.element(tab))

    @allure.step('Filling model name with "{model}"')
    def fill_model_tab(self, model):
        self._input(self.element(self.MODEL_FIELD), model)

    @allure.step('Delete "{product_name}" product')
    def delete_item(self, product_name):
        """Удалить продукт. Сначала выбираем конкретный продукт с конкретным именем, затем удаляем"""

        pick_item = (By.XPATH, f"//*[contains(text(), '{product_name}')]/parent::tr//*[@name='selected[]']")
        self.click(self.element(pick_item))
        self.click(self.element(self.DELETE_ITEM))
