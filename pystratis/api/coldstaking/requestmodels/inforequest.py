from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class InfoRequest(Model):
    """A request model for the coldstaking/cold-staking-info endpoint.

    Args:
        wallet_name (str): The wallet name.
    """
    wallet_name: str = Field(alias='WalletName')
