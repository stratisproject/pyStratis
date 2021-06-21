from typing import List
from pydantic import BaseModel
from .addressmodel import AddressModel


class AddressesModel(BaseModel):
    """An AddressesModel."""
    addresses: List[AddressModel]

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
