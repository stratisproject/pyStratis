from pydantic import Field
from pybitcoin import Address, Model


class ReceivedByAddressRequest(Model):
    """A ReceivedByAddressRequest."""
    address: Address = Field(alias='Address')
