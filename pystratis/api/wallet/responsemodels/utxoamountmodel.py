from pystratis.api import Model
from pystratis.core.types import Money
from pydantic import Field


class UtxoAmountModel(Model):
    """A pydantic model representing a utxo amount."""
    amount: Money = Field(alias='Amount')
    """The total amount in the utxos."""
    count: int = Field(alias='Count')
    """The number of utxos included in the count."""
