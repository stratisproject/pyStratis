from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class BalancesRequest(Model):
    """A request model for the smartcontracts/address-balanes endpoint.

    Args:
        wallet_name (str): The wallet name.
    """
    wallet_name: str = Field(alias='walletName')
