from typing import Optional
from pydantic import Field, conint
from pybitcoin import Address, Model


class HistoryRequest(Model):
    """A HistoryRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    address: Optional[Address] = Field(alias='Address')
    skip: Optional[conint(ge=0)] = Field(alias='Skip')
    take: Optional[conint(ge=0)] = Field(alias='Take')
    prev_output_tx_time: Optional[conint(ge=0)] = Field(alias='PrevOutputTxTime')
    prev_output_index: Optional[conint(ge=0)] = Field(alias='PrevOutputIndex')
    search_query: Optional[str] = Field(alias='SearchQuery')
