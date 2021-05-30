from pydantic import Field
from pybitcoin import Address, Model


class VerifyMessageRequest(Model):
    """A VerifyMessageRequest."""
    signature: str
    external_address: Address = Field(alias='externalAddress')
    message: str
