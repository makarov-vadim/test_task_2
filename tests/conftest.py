import pytest
from requests import options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


# @pytest.fixture(scope="session")
# def browser():
#    print("\nstart browser for test..")
#    options = Options()
#    options.add_argument('--headless')
#    browser = webdriver.Chrome(options=options)
#    yield browser
#    print("\nquit browser..")
#    browser.quit()

@pytest.fixture(scope="session")
def browser():
   print("\nstart browser for test..")
   options = webdriver.ChromeOptions()
   options.add_argument('--headless')
   browser = webdriver.Remote(
      command_executor="http://localhost:4444",
      options=options
   )
   yield browser
   print("\nquit browser..")
   browser.quit()

@pytest.fixture(scope="session")
def main_page(browser):
   main_page = MainPage(browser)
   yield main_page