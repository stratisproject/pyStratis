from pydantic import Field
from pystratis.core.types import Address
from pystratis.api import Model


class AddressDescriptor(Model):
    """An AddressDescriptor"""
    address: Address
    key_path: str = Field(alias='keyPath')
    address_type: str = Field(alias='addressType')
