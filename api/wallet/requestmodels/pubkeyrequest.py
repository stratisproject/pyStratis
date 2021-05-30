from pydantic import Field
from pybitcoin import Address, Model


class PubKeyRequest(Model):
    """A PubKeyRequest."""
    wallet_name: str = Field(alias='walletName')
    external_address: Address = Field(alias='externalAddress')
