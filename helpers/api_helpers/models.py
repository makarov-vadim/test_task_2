from pydantic import BaseModel


class AdditionModel(BaseModel):
    """Класс, описывающий модель атрибута addition сущности"""
    additional_info: str
    additional_number: int


class EssenceModel(BaseModel):
    """Класс, описывающий модель сущности"""
    addition: AdditionModel
    important_numbers: list
    title: str
    verified: bool