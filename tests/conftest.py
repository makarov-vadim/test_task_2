import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.requests.service_api import ServiceApi
from helpers.api_helpers.api_helper import get_essence
from pages.main_page import MainPage


@pytest.fixture(scope="session")
def browser():
   options = Options()
   options.add_argument('--headless')
   browser = webdriver.Chrome(options=options)
   yield browser
   browser.quit()

# @pytest.fixture(scope="session")
# def browser():
#    print("\nstart browser for test..")
#    options = webdriver.ChromeOptions()
#    # options.add_argument('--headless')
#    browser = webdriver.Remote(
#       command_executor="http://localhost:4444",
#       options=options
#    )
#    yield browser
#    print("\nquit browser..")
#    browser.quit()


@pytest.fixture(scope="session")
def main_page(browser):
   main_page = MainPage(browser)
   yield main_page


@pytest.fixture(scope="session")
def service():
    service = ServiceApi()
    yield service


@pytest.fixture(scope="session")
def obj_id(service):
   essence = get_essence()
   response = service.post_object(essence.model_dump())
   yield response.json()
   service.delete_object(response.json())


# @pytest.fixture(scope="session")
# def list_essences(service):
#    list_obj_id = []
#    essences = []
#    for _ in range(3):
#       essence = get_essence()
#       response = service.post_object(essence.model_dump())
#       list_obj_id.append(response)
#       essences.append(essence)
#
#    yield essences
#
#    for obj_id in list_obj_id:
#       service.delete_object(obj_id)

