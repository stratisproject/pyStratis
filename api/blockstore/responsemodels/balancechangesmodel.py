from typing import Optional
from pybitcoin import Model
from pydantic import conint, Field


class BalanceChangesModel(Model):
    """A BalanceChangesModel."""
    deposited: Optional[bool]
    satoshi: conint(ge=0)
    balance_changed_height: Optional[conint(ge=0)] = Field(alias='balanceChangedHeight')
