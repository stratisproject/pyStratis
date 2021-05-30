from pydantic import SecretStr, Field
from pybitcoin import Address, Model


class PrivateKeyRequest(Model):
    """A PrivateKeyRequest."""
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
    address: Address
