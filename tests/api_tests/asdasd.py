from helpers.api_helpers.api_helper import get_essence


data = get_essence().model_dump()
print(data)