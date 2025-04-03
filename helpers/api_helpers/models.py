from pydantic import BaseModel


class AdditionModel(BaseModel):
    additional_info: str
    additional_number: int


class EssenceModel(BaseModel):
    addition: AdditionModel
    important_numbers: list
    title: str
    verified: bool