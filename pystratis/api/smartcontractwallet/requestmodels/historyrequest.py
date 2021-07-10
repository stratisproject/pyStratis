from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Address


# noinspection PyUnresolvedReferences
class HistoryRequest(Model):
    """A request model for the smartcontractwallet/history endpoint.

    Args:
        wallet_name (str): The wallet name.
        address (Address): The address to query the history.
        skip (conint(ge=0), optional): Skip this many items. Default=0.
        take (conint(ge=0), optional): Take this many items.
    """
    wallet_name: str = Field(alias='WalletName')
    address: Address
    skip: Optional[conint(ge=0)] = Field(default=0, alias='Skip')
    take: Optional[conint(ge=0)] = Field(alias='Take')
