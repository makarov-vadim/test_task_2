from helpers.api_helpers.api_helper import get_essence



class TestsApi:
    def test_post(self, service):
        essence = get_essence().model_dump()
        response = service.post_object(essence)
        print(f'\n{response}')

    def test_get(self, service):
        response = service.get_object(10)
        print(f'\n{response}')

    def test_get_all(self, service):
        response = service.get_all_objects()
        print(f'\n{response}')

    def test_delete(self, service):
        response = service.delete_object(7)
        print(f'\n{repr(response)}')

    def test_patch(self, service):
        essence = get_essence().model_dump()
        response = service.patch_object(6, essence)
        print(f'\n{repr(response)}')
        print(f'\n{service.get_object(6)}')