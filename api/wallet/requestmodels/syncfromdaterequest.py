from typing import Optional
from pydantic import Field
from pybitcoin import Model


class SyncFromDateRequest(Model):
    """A SyncFromDateRequest."""
    date: str
    all: Optional[bool] = True
    wallet_name: str = Field(alias='walletName')
