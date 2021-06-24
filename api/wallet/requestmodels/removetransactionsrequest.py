from typing import Optional, List
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class RemoveTransactionsRequest(Model):
    """A request model for the wallet/remove-transactions endpoint.

    Args:
        wallet_name: str = Field(alias='WalletName')
        ids: Optional[List[uint256]]
        from_date: Optional[str] = Field(alias='fromDate')
        all: Optional[bool] = False
        resync: Optional[bool] = Field(default=True, alias='ReSync')
    """
    wallet_name: str = Field(alias='WalletName')
    ids: Optional[List[uint256]]
    from_date: Optional[str] = Field(alias='fromDate')
    all: Optional[bool] = False
    resync: Optional[bool] = Field(default=True, alias='ReSync')
