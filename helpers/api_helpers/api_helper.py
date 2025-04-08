from random import choice, randint, choices
from typing import Any

from faker import Faker

from helpers.api_helpers.models import AdditionModel, EssenceModel


def get_additional_info() -> str:
    """Функция, генерирующая additional info для сущности"""
    return Faker('ru_RU').job()


def get_additional_number() -> int:
    """Функция, генерирующая additional number для сущности"""
    return randint(0, 1000)


def get_important_numbers() -> list[int]:
    """Функция, генерирующая important numbers для сущности"""
    return [randint(0, 100) for _ in range(5)]


def get_title() -> str:
    """Функция, генерирующая title для сущности"""
    return Faker('ru_RU').name()


def get_verified() -> bool:
    """Функция, генерирующая verified для сущности"""
    return choice([False, True])


def get_data(attr_name: str) -> Any:
    """Функция, генерирующая необходимый атрибут для сущности"""
    functions = {
        "additional_info": get_additional_info,
        "additional_number": get_additional_number,
        "addition": get_addition,
        "important_numbers": get_important_numbers,
        "title": get_title,
        "verified": get_verified
    }
    return functions[attr_name]()


def get_update_data() -> dict[str, Any]:
    """Функция, генерирующая атрибуты, необходимые для обновления сущности"""
    attr_names = [
        "additional_info",
        "additional_number",
        "addition",
        "important_numbers",
        "title",
        "verified"
    ]
    updated_fields = choices(attr_names, k=randint(1, len(attr_names)))
    updated_data = {field: get_data(field) for field in updated_fields}
    return updated_data


def get_addition() -> AdditionModel:
    """Функция, генерирующая модель AdditionModel"""
    addition_model_data = {
        "additional_info": get_data("additional_info"),
        "additional_number": get_data("additional_number")
    }
    return AdditionModel(**addition_model_data)


def get_essence() -> EssenceModel:
    """Функция, генерирующая модель EssenceModel"""
    essence_model_data = {
        "addition": get_data("addition"),
        "important_numbers": get_data("important_numbers"),
        "title": get_data("title"),
        "verified": get_data("verified")
    }
    return EssenceModel(**essence_model_data)


def get_essence_from_response(response:dict[str, Any]) -> EssenceModel:
    """Функция, возвращающая модель EssenceModel, считанную с сервиса"""
    essence_model_data = {
        "addition": AdditionModel(**response["addition"]),
        "important_numbers": response["important_numbers"],
        "title": response["title"],
        "verified": response["verified"]
    }
    return EssenceModel(**essence_model_data)


def update_essence(essence:EssenceModel) -> EssenceModel:
    """Функция, возвращающая обновленную модель EssenceModel"""
    new_attrs = get_update_data()

    new_addition = essence.addition.model_copy(update=new_attrs)
    new_attrs["addition"] = new_addition
    new_essence = essence.model_copy(update=new_attrs)

    return new_essence
