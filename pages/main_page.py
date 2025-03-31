from selenium.webdriver.common.by import By

from config.config import URLS
from helpers.help_functions import get_first_name, get_post_code
from pages.base_page import BasePage


class Locators:
    '''Класс, описывающий локаторы для поиска необходимых элементов'''
    # ПОМЕНЯТЬ ЛОКАТОРЫ
    LCTR_TAB_ADD_CUSTOMER = (By.CSS_SELECTOR, "[ng-click='addCust()']")
    LCTR_FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='First Name']")
    LCTR_FIELD_LAST_NAME = (By.CSS_SELECTOR, "[placeholder='Last Name']")
    LCTR_FIELD_POST_CODE = (By.CSS_SELECTOR, "[placeholder='Post Code']")
    LCTR_BTN_ADD_CUSTOMER = (By.CSS_SELECTOR, "button.btn.btn-default")
    LCTR_TAB_CUSTOMERS = (By.CSS_SELECTOR, "[ng-click='showCust()']")
    LCTR_SORT_FIRST_NAME = (By.XPATH, "//tr/td[1]/a")
    LCTR_CUSTOMERS_TABLE = (By.XPATH, '//div/table/tbody/tr')


class MainPage(BasePage):
    '''Класс, описывающий главную страницу'''
    def __init__(self, driver):
        url = URLS.URL_MAIN_PAGE
        super().__init__(driver, url)

    def enter_word(self, locator, word):
        '''Метод, позволяющий ввести данные в поле'''
        search_field = self.click_element(locator)
        search_field.send_keys(word)
        return search_field

    def open_tab_add_customer(self):
        self.click_element(Locators.LCTR_TAB_ADD_CUSTOMER)

    def open_tab_customers(self):
        self.click_element(Locators.LCTR_TAB_CUSTOMERS)

    def filling_fields(self):
        post_code = get_post_code()
        first_name = get_first_name(post_code)
        last_name = first_name[::-1]

        self.enter_word(Locators.LCTR_FIELD_FIRST_NAME, first_name)
        self.enter_word(Locators.LCTR_FIELD_LAST_NAME, last_name)
        self.enter_word(Locators.LCTR_FIELD_POST_CODE, post_code)

    def click_add_customer(self):
        self.click_element(Locators.LCTR_BTN_ADD_CUSTOMER)

    def read_alert(self):
        alert_obj = self.driver.switch_to.alert
        msg = alert_obj.text
        alert_obj.accept()
        return msg

    def sort_by_first_name(self):
        self.click_element(Locators.LCTR_SORT_FIRST_NAME)

    def get_customers_names(self) -> list[str]:
        locator = Locators.LCTR_CUSTOMERS_TABLE
        customers_names = []

        rows = len(self.find_elements((locator[0], f'{locator[1]}')))

        for r in range(1, rows + 1):
            first_name = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{1}]')).text
            customers_names.append(first_name)

        return customers_names

    def delete_customer(self, name_to_delete):
        locator = Locators.LCTR_CUSTOMERS_TABLE

        rows = len(self.find_elements((locator[0], f'{locator[1]}')))
        columns = len(self.find_elements((locator[0], f'{locator[1]}[1]/td')))

        for r in range(1, rows + 1):
            first_name = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{1}]')).text
            if first_name == name_to_delete:
                delete_btn = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{columns}]/button'))
                return delete_btn


    def get_customers_del_btns(self):
        '''Метод, который считывает таблицу "Customer" и возвращает словарь,
        в котором ключом является имя (First Name) клиента,
        а значением - клавиша "Delete", удаляющая этого клиента из таблицы "Customer"'''
        locator = Locators.LCTR_CUSTOMERS_TABLE
        customers_del_btns = {}

        rows = len(self.find_elements((locator[0], f'{locator[1]}')))
        columns = len(self.find_elements((locator[0], f'{locator[1]}[1]/td')))

        for r in range(1, rows + 1):
            first_name = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{1}]')).text
            delete_btn = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{columns}]/button'))
            customers_del_btns[first_name] = delete_btn

        return customers_del_btns