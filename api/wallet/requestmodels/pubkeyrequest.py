from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class PubKeyRequest(Model):
    """A PubKeyRequest."""
    wallet_name: str = Field(alias='walletName')
    external_address: Address = Field(alias='externalAddress')
