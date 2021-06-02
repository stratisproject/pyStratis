from pydantic import Field
from pybitcoin import Address, Model


class ValidateAddressModel(Model):
    """A ValidateAddressModel."""
    isvalid: bool
    address: Address
    scriptPubKey: str = Field(alias='scriptPubKey')
    isscript: bool
    iswitness: bool
