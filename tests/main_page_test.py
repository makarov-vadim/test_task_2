from re import match

import allure

from helpers.help_functions import get_name_to_delete
from pages.main_page import MainPage


@allure.epic("TestsMainPage")
@allure.feature("Test Cases")
class TestsMainPage:
    """Класс, описывающий автотест страницы MainPage"""
    @allure.story("Создание клиента Add Customer")
    def test_case_1(self, browser):
        """Тест-кейс 1. Создание клиента (Add Customer)"""
        main_page = MainPage(browser)
        main_page.go_to_site()

        main_page.open_tab_add_customer()
        main_page.filling_fields()
        main_page.click_add_customer()
        alert_text = main_page.read_alert()

        assert bool(match(r'Customer added successfully', alert_text)), "Клиент не добавлен"

    @allure.story("Сортировка клиентов по имени First Name")
    def test_case_2(self, browser):
        """Тест-кейс 2. Сортировка клиентов по имени (First Name)"""
        main_page = MainPage(browser)

        main_page.open_tab_customers()
        main_page.sort_by_first_name()

        customers_names = main_page.get_customers_names()
        sorted_names = sorted(customers_names, key=lambda name: name.lower(), reverse=True)
        assert sorted_names == customers_names, "Клиенты не отсортированы"

    # @allure.story("Удаление клиента")
    # def test_case_3(self, browser):
    #     """Тест-кейс 3. Удаление клиента"""
    #     main_page = MainPage(browser)
    #
    #     customers_names = main_page.get_customers_names()
    #     name_to_delete = get_name_to_delete(customers_names)
    #
    #     main_page.delete_customer(name_to_delete)
    #
    #     assert name_to_delete not in main_page.get_customers_names(), f"Клиент {name_to_delete} не удален"
    #







