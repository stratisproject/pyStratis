from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class VerifyMessageRequest(Model):
    """A VerifyMessageRequest."""
    signature: str
    external_address: Address = Field(alias='externalAddress')
    message: str
