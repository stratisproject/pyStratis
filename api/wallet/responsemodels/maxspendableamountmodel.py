from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Money


class MaxSpendableAmountModel(Model):
    """A MaxSpendableAmountModel."""
    max_spendable_amount: Optional[Money] = Field(alias='MaxSpendableAmount')
    fee: Optional[Money] = Field(alias='Fee')
