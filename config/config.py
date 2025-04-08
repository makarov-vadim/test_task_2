class UI_URLS:
    """Класс, описывающий набор url-адресов, необходимых для UI тестов"""
    # url-адрес главной страницы
    URL_MAIN_PAGE = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

class API_URLS:
    """Класс, описывающий набор url-адресов, необходимых для API тестов"""
    # url-адрес хоста сервиса
    HOST_URL = "http://localhost:8080"

    # url-адрес точки доступа для создания сущности
    POST_URL = f"{HOST_URL}/api/create"

    # url-адрес точки доступа для получения сущности
    GET_URL = f"{HOST_URL}/api/get/" # при использовании необходимо добавлять id

    # url-адрес точки доступа для получения всех сущностей
    GET_ALL_URL = f"{HOST_URL}/api/getAll"

    # url-адрес точки доступа для удаления сущности
    DELETE_URL = f"{HOST_URL}/api/delete/" # при использовании необходимо добавлять id

    # url-адрес точки доступа для обновления сущности
    PATCH_URL = f"{HOST_URL}/api/patch/" # при использовании необходимо добавлять id



