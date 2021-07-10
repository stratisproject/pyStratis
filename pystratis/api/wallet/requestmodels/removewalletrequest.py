from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class RemoveWalletRequest(Model):
    """A request model for the wallet/remove-wallet endpoint.

    Args:
        wallet_name (str): The wallet name.
    """
    wallet_name: str = Field(alias='WalletName')
