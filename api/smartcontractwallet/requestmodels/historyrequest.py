from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import Address


class HistoryRequest(Model):
    """A HistoryRequest."""
    wallet_name: str = Field(alias='WalletName')
    address: Address
    skip: Optional[conint(ge=0)] = Field(default=0, alias='Skip')
    take: Optional[conint(ge=0)] = Field(alias='Take')
