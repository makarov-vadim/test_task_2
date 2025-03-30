import allure

from helpers.help_functions import get_first_name, get_name_to_delete, get_post_code
from pages.main_page import Locators, MainPage
from re import  match


@allure.epic('Test_UI')
@allure.feature('Test Cases')
class TestsMainPage:
    '''Класс, описывающий автотест страницы MainPage'''
    @allure.story('Создание клиента (Add Customer)')
    @allure.step('Шаги')
    def test_case_1(self, browser):
        '''Тест-кейс 1. Создание клиента (Add Customer)'''
        self.main_page = MainPage(browser)
        self.main_page.go_to_site()

        with allure.step('Клик по вкладке Add "Customer"'):
            self.main_page.click_element(Locators.LCTR_TAB_ADD_CUSTOMER)

        post_code = get_post_code()
        first_name = get_first_name(post_code)
        last_name = first_name[::-1]

        with allure.step('Ввод данных в поля "First Name", "Last Name", "Post Code"'):
            self.main_page.enter_word(Locators.LCTR_FIELD_FIRST_NAME, first_name)
            self.main_page.enter_word(Locators.LCTR_FIELD_LAST_NAME, last_name)
            self.main_page.enter_word(Locators.LCTR_FIELD_POST_CODE, post_code)

        with allure.step('Клик по кнопке "Add Customer"'):
            self.main_page.click_element(Locators.LCTR_BTN_ADD_CUSTOMER)

        alert_obj = browser.switch_to.alert
        msg = alert_obj.text
        alert_obj.accept()
        assert bool(match(r'Customer added successfully', msg))

    @allure.epic('Test_UI')
    @allure.feature('Test Cases')
    @allure.story('Сортировка клиентов по имени (First Name)')
    @allure.step('Шаги')
    def test_case_2(self, browser):
        '''Тест-кейс 2. Сортировка клиентов по имени (First Name)'''
        main_page = MainPage(browser)
        with allure.step('Клик по вкладке "Customer"'):
            main_page.click_element(Locators.LCTR_TAB_CUSTOMERS)

        with allure.step('Первый клик по заголовку столбца "First Name"'):
            main_page.click_element(Locators.LCTR_SORT_FIRST_NAME)

        with allure.step('Второй клик по заголовку столбца "First Name"'):
            main_page.click_element(Locators.LCTR_SORT_FIRST_NAME)

        customers_del_btns = main_page.get_customers_del_btns()
        sorted_names = sorted(customers_del_btns.keys(), key=str.lower)
        assert sorted_names == list(customers_del_btns.keys())

    @allure.epic('Test_UI')
    @allure.feature('Test Cases')
    @allure.story('Удаление клиента')
    @allure.step('Шаги')
    def test_case_3(self, browser):
        '''Тест-кейс 3. Удаление клиента'''
        main_page = MainPage(browser)

        with allure.step('Поиск клиента для удаления'):
            customers_del_btns = main_page.get_customers_del_btns()
            name_to_delete = get_name_to_delete(customers_del_btns.keys())

        with allure.step('Удаление выбранного клиента'):
            customers_del_btns[name_to_delete].click()

        assert name_to_delete not in main_page.get_customers_del_btns()








