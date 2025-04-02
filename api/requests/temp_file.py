from api.requests.service_api import ServiceApi

x = ServiceApi()

data = {"addition": {"additional_info": "Заголовок №2", "additional_number": 565},"important_numbers": [42, 87, 15], "title": "Заголовок сущности", "verified": True}
data_2 = {"addition": {"additional_info": "------------adasd-----", "additional_number": 796},"important_numbers": [42, 87, 15], "title": "Заголовок сущности", "verified": True}

id = 5

print(x.get_all_objects())
print(x.get_object(id))

x.delete_object(id)
print(x.get_object(id))


