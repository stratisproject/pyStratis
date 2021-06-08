from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class ReceivedByAddressRequest(Model):
    """A ReceivedByAddressRequest."""
    address: Address = Field(alias='Address')
