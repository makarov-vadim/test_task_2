from helpers.api_helpers.models import AdditionModel, EssenceModel
from random import choice, randint
from faker import Faker

def get_additional_info():
    return Faker('ru_RU').job()

def get_additional_number():
    return randint(0, 1000)

def get_important_numbers():
    return [randint(0, 100) for _ in range(5)]

def get_title():
    return Faker('ru_RU').name()

def get_verified():
    return choice([False, True])


def get_addition():
    addition_model_data = {
        "additional_info": get_additional_info(),
        "additional_number": get_additional_number()
    }
    return AdditionModel(**addition_model_data)

def get_essence():
    essence_model_data = {
        "addition": get_addition(),
        "important_numbers": get_important_numbers(),
        "title": get_title(),
        "verified": get_verified()
    }
    return EssenceModel(**essence_model_data)








