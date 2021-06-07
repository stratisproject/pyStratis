from typing import Optional
from pybitcoin import Model
from pybitcoin.types import Money
from pydantic import conint, Field


class BalanceChangesModel(Model):
    """A BalanceChangesModel."""
    deposited: Optional[bool]
    satoshi: Optional[Money]
    balance_changed_height: Optional[conint(ge=0)] = Field(alias='balanceChangedHeight')
