from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address


class ValidateAddressModel(Model):
    """A pydantic model for address validation."""
    isvalid: bool
    """True if the address is valid."""
    address: Address
    """The address."""
    scriptPubKey: str = Field(alias='scriptPubKey')
    """The scriptPubKey."""
    isscript: bool
    """True if is a script address."""
    iswitness: bool
    """True if is a witness address."""
