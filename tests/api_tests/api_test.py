import allure

from helpers.api_helpers.api_helper import get_essence, get_essence_from_response, update_essence


@allure.epic("API_Tests")
@allure.feature("Test Cases")
class TestsApi:
    """Класс, описывающий автотест страницы сервиса ServiceApi"""
    @allure.story("Тестирование точки доступа GETALL")
    def test_get_all(self, service, essences):
        """Тест-кейс 1. Тестирование точки доступа GETALL"""
        response = service.get_all_objects()
        essences_from_response = [get_essence_from_response(entity) for entity in response.json()["entity"]]

        assert response.status_code == 200, "Неверный код статуса для получения всех сущностей"
        assert essences == essences_from_response, "Список полученных сущностей не совпадает со списком созданных"


    @allure.story("Тестирование точки доступа GET")
    def test_get(self, service, obj_id):
        """Тест-кейс 2. Тестирование точки доступа GET"""
        response = service.get_object(obj_id)

        assert response.status_code == 200, "Неверный код статуса для получения сущности"
        assert response.json()["id"]== obj_id, "Несоответствие id созданной и полученной сущности"


    @allure.story("Тестирование точки доступа POST")
    def test_post(self, service):
        """Тест-кейс 3. Тестирование точки доступа POST"""
        essence = get_essence()

        response = service.post_object(essence.model_dump())
        response_get = service.get_object(response.json())
        service.delete_object(response_get.json()["id"])

        essence_get = get_essence_from_response(response_get.json())

        assert response.status_code == 200, "Неверный код статуса для создания сущности"
        assert response_get.status_code == 200, "Неверный код статуса для получения созданной сущности"
        assert essence == essence_get, "Несоответствие созданной и полученной сущности"


    @allure.story("Тестирование точки доступа PATCH")
    def test_patch(self, service, obj_id):
        """Тест-кейс 4. Тестирование точки доступа PATCH"""
        essence = get_essence_from_response(service.get_object(obj_id).json())
        new_essence = update_essence(essence)

        response = service.patch_object(obj_id, new_essence.model_dump())

        new_essence_get = get_essence_from_response(service.get_object(obj_id).json())

        assert response.status_code == 204, "Неверный код статуса для обновления сущности"
        assert new_essence == new_essence_get, "Сущность не обновлена"


    @allure.story("Тестирование точки доступа DELETE")
    def test_delete(self, service, obj_id):
        """Тест-кейс 5. Тестирование точки доступа DELETE"""
        response = service.delete_object(obj_id)

        response_get = service.get_object(obj_id)

        error_msg = lambda: "error" in response_get.json() and response_get.json()["error"] == "no rows in result set"
        assert response.status_code == 204, "Неверный код статуса для удаления сущности"
        assert error_msg(), "Сущность не удалена"
