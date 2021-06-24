from pydantic import Field, SecretStr
from pybitcoin import Model


class GetUnusedAccountRequest(Model):
    """A request model for the wallet/account endpoint.

    Args:
        password: SecretStr
        wallet_name: str = Field(alias='walletName')
    """
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
