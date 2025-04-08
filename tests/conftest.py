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
    service.delete_all_objects()
    yield service
    service.delete_all_objects()


@pytest.fixture(scope="session")
def obj_id(service):
    essence = get_essence()
    response = service.post_object(essence.model_dump())
    yield response.json()
    service.delete_object(response.json())


@pytest.fixture(scope="session")
def created_essences(service):
    essences = {}
    for _ in range(3):
        essence = get_essence()
        essence_id = service.post_object(essence.model_dump()).json()
        essences[essence_id] = essence

    yield list(essences.values())

    for essence_id in essences:
        service.delete_object(essence_id)
