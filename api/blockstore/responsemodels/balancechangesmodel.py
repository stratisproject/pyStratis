from pybitcoin import Model
from pybitcoin.types import Money
from pydantic import conint, Field


class BalanceChangesModel(Model):
    """A BalanceChangesModel."""
    deposited: bool
    satoshi: Money
    balance_changed_height: conint(ge=0) = Field(alias='balanceChangedHeight')
