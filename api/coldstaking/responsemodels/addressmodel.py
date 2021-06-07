from typing import Optional
from pybitcoin import Model, Address


class AddressModel(Model):
    """An AddressModel."""
    address: Optional[Address]
