from config.config import URLS
from helpers.base_page import BasePage
from selenium.webdriver.common.by import By


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