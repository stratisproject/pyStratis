from typing import Optional
from pybitcoin import Model
from pybitcoin.types import Address


class AddressModel(Model):
    """An AddressModel."""
    address: Optional[Address]
