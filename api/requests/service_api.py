from api.requests.base_requests import BaseApi
from  config.config import API_URLS

class ServiceApi(BaseApi):
    def __init__(self):
        self.url = API_URLS.HOST_URL


    def post_object(self, data):
        response = self._request_post(url=API_URLS.POST_URL, json=data)
        return response.json()

    def get_object(self, obj_id):
        return self._request_get(url=API_URLS.GET_URL.format(obj_id)).json()

    def get_all_objects(self):
        return self._request_get(url=API_URLS.GET_ALL_URL).json()

    def delete_object(self, obj_id):
        response = self._request_delete(url=API_URLS.DELETE_URL.format(obj_id))
        return response

    def patch_object(self, obj_id, data):
        response = self._request_patch(url=API_URLS.PATCH_URL.format(obj_id), json=data)
        return response
