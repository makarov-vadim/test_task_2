import requests


class BaseApi:
    def _request_post(self, **kwargs):
        return requests.post(**kwargs)

    def _request_get(self, **kwargs):
        return requests.get(**kwargs)

    def _request_delete(self, **kwargs):
        return requests.delete(**kwargs)

    def _request_patch(self, **kwargs):
        return requests.patch(**kwargs)
