from typing import List
from pystratis.api import Model
from .addressmodel import AddressModel


class AddressesModel(Model):
    """An AddressesModel."""
    addresses: List[AddressModel]
