from pydantic import Field, SecretStr
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class GetUnusedAccountRequest(Model):
    """A request model for the wallet/account endpoint.

    Args:
        password (str): The wallet password.
        wallet_name (str): The wallet name.
    """
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
