from pydantic import SecretStr, Field
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class PrivateKeyRequest(Model):
    """A request model for the wallet/privatekey endpoint.

    Args:
        password (str): The wallet password.
        wallet_name (str): The wallet name.
        address (Address): The address to request a private key for.
    """
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
    address: Address
