from typing import Optional, List
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import uint256


# noinspection PyUnresolvedReferences
class RemoveTransactionsRequest(Model):
    """A request model for the wallet/remove-transactions endpoint.

    Args:
        wallet_name (str): The wallet name.
        ids (List[uint256], optional): A list of transaction ids to remove.
        from_date (str, optional): An option to remove transactions after given date.
        remove_all (bool, optional): An option to remove all transactions. Default=False.
        resync (bool, optional): If True, resyncs wallet after items removed. Default=True.
    """
    wallet_name: str = Field(alias='WalletName')
    ids: Optional[List[uint256]]
    from_date: Optional[str] = Field(default=None, alias='fromDate')
    remove_all: Optional[bool] = Field(default=False, alias='all')
    resync: Optional[bool] = Field(default=True, alias='ReSync')
