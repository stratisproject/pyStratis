from typing import Optional
from pydantic import Field
from pybitcoin import Model


class SyncFromDateRequest(Model):
    """A request model for the wallet/sync-from-date endpoint.

    Args:
        date: str
        all: Optional[bool] = True
        wallet_name: str = Field(alias='walletName')
    """
    date: str
    all: Optional[bool] = True
    wallet_name: str = Field(alias='walletName')
