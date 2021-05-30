from typing import Optional, List
from pydantic import Field
from pybitcoin import Model


class RemoveTransactionsRequest(Model):
    """A RemoveTransactionsRequest."""
    wallet_name: str = Field(alias='WalletName')
    ids: List[str]
    from_date: str = Field(alias='fromDate')
    all: Optional[bool] = False
    resync: Optional[bool] = Field(default=True, alias='ReSync')
