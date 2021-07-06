from pystratis.api import Model
from pydantic import Field


class BalanceChangesModel(Model):
    """A pydantic model representing changes in balance at a given address."""
    deposited: bool
    """If true, amount was received. False if value was withdrawn."""
    satoshi: int
    """The value of the amount changed, in satoshi."""
    balance_changed_height: int = Field(alias='balanceChangedHeight')
    """The height of the block containing the transaction."""
