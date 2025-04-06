import requests


class BaseApi:
    """Класс, описывающий базовый сервис, который предоставляет
    точки доступа для управления сущностями в базе данных PostgreSQL"""

    def _request_post(self, **kwargs):
        """Метод, создающий сущность на сервисе"""
        return requests.post(**kwargs)

    def _request_get(self, **kwargs):
        """Метод, получающий сущность из сервиса"""
        return requests.get(**kwargs)

    def _request_delete(self, **kwargs):
        """Метод, удаляющий сущность на сервисе"""
        return requests.delete(**kwargs)

    def _request_patch(self, **kwargs):
        """Метод, обновляющий сущность на сервисе"""
        return requests.patch(**kwargs)
