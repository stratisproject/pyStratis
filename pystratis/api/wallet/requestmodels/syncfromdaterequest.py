from typing import Optional
from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class SyncFromDateRequest(Model):
    """A request model for the wallet/sync-from-date endpoint.

    Args:
        date (str): The date to sync from in YYYY-MM-DDTHH:MM:SS format.
        all_transactions (bool, optional): If True, sync all transactions. Default=True.
        wallet_name (str): The wallet name.
    """
    date: str
    all_transactions: Optional[bool] = Field(default=True, alias='all')
    wallet_name: str = Field(alias='walletName')
