from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс, описывающий базовую страницу"""

    def __init__(self, driver, url, timeout=10):
        self.timeout = timeout
        self.driver = driver
        self.url = url

    def go_to_site(self):
        """Метод, который открывает и разворачивает страниц"""
        self.driver.maximize_window()
        return self.driver.get(self.url)

    def find_element(self, locator):
        """Метод поиска элемента на странице"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator):
        """Метод поиска группы элементов на странице"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def click_element(self, locator):
        '''Метод, позволяющий кликнуть по элементу'''
        clickable_element = self.find_element(locator)
        clickable_element.click()
        return clickable_element
