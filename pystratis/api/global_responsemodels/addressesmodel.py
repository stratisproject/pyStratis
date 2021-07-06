from typing import List
from pystratis.api import Model
from .addressmodel import AddressModel


class AddressesModel(Model):
    """A pydantic model for a list of addressmodels."""
    addresses: List[AddressModel]
    """The list of address models."""
