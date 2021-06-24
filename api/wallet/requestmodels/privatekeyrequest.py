from pydantic import SecretStr, Field
from pybitcoin import Model
from pybitcoin.types import Address


class PrivateKeyRequest(Model):
    """A request model for the wallet/privatekey endpoint.

    Args:
        password: SecretStr
        wallet_name: str = Field(alias='walletName')
        address: Address
    """
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
    address: Address
