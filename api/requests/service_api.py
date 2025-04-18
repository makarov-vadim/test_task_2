import allure

from api.requests.base_requests import BaseApi
from config.config import API_URLS


class ServiceApi(BaseApi):
    """Класс, описывающий тестовый сервис, который предоставляет
    точки доступа для управления сущностями в базе данных PostgreSQL"""
    def __init__(self):
        self.url = API_URLS.HOST_URL

    @allure.step("Создание сущности")
    def post_object(self, data):
        """Метод, создающий сущность на сервисе"""
        return self._request_post(url=API_URLS.POST_URL, json=data)

    @allure.step("Получение сущности")
    def get_object(self, object_id):
        """Метод, получающий сущность из сервиса"""
        return self._request_get(url=f"{API_URLS.GET_URL}{object_id}")

    @allure.step("Получение всех сущностей")
    def get_all_objects(self):
        """Метод, получающий все сущности из сервиса"""
        return self._request_get(url=API_URLS.GET_ALL_URL)

    @allure.step("Удаление сущности")
    def delete_object(self, object_id):
        """Метод, удаляющий сущность на сервисе"""
        return self._request_delete(url=f"{API_URLS.DELETE_URL}{object_id}")

    @allure.step("Обновление сущности")
    def patch_object(self, object_id, data):
        """Метод, обновляющий сущность на сервисе"""
        return self._request_patch(url=f"{API_URLS.PATCH_URL}{object_id}", json=data)

    @allure.step("Удаление всех сущностей")
    def delete_all_objects(self):
        """Метод, удаляющий все сущности на сервисе"""
        response_get_all = self.get_all_objects()
        for entity in response_get_all.json()["entity"]:
            entity_id = entity["id"]
            self.delete_object(entity_id)
