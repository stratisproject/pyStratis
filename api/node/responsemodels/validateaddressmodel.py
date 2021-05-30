from pydantic import Field
from pybitcoin import Address, Model
from pybitcoin.types import hexstr


class ValidateAddressModel(Model):
    """A ValidateAddressModel."""
    isvalid: bool
    address: Address
    scriptPubKey: hexstr = Field(alias='scriptPubKey')
    isscript: bool
    iswitness: bool
