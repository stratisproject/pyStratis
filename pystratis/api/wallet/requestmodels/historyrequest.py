from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class HistoryRequest(Model):
    """A request model for the wallet/history endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        address (Address, optional): The address to query the history.
        skip (conint(ge=0)): The number of history items to skip.
        take (conint(ge=0)): The number of history items to take.
        prev_output_tx_time (conint(ge=0), optional): The previous output transaction time.
        prev_output_index (conint(ge=0), optional): The previous output transaction index.
        search_query (str, optional): A search query.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    address: Optional[Address] = Field(alias='Address')
    skip: Optional[conint(ge=0)] = Field(alias='Skip')
    take: Optional[conint(ge=0)] = Field(alias='Take')
    prev_output_tx_time: Optional[conint(ge=0)] = Field(alias='PrevOutputTxTime')
    prev_output_index: Optional[conint(ge=0)] = Field(alias='PrevOutputIndex')
    search_query: Optional[str] = Field(alias='SearchQuery')
