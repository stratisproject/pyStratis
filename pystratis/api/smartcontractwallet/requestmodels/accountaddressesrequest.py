from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class AccountAddressesRequest(Model):
    """A request model for the smartcontractwallet/account-addresses endpoint.

    Args:
        wallet_name (str): The wallet name.
    """
    wallet_name: str = Field(alias='walletName')
