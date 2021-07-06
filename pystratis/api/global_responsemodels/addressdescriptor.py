from pydantic import Field
from pystratis.core.types import Address
from pystratis.api import Model


class AddressDescriptor(Model):
    """A pydantic model of an address descriptor."""
    address: Address
    """The address."""
    key_path: str = Field(alias='keyPath')
    """The key path."""
    address_type: str = Field(alias='addressType')
    """The address type."""
