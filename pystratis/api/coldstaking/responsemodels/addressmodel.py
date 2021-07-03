from typing import Optional
from pystratis.core import Model
from pystratis.core.types import Address


class AddressModel(Model):
    """An AddressModel."""
    address: Optional[Address]
