import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


@pytest.fixture(scope="session")
def browser():
   print("\nstart browser for test..")
   options = Options()
   options.add_argument('--headless')
   browser = webdriver.Chrome(options=options)
   yield browser
   print("\nquit browser..")
   browser.quit()

@pytest.fixture(scope="session")
def main_page(browser):
   main_page = MainPage(browser)
   yield main_page