from typing import Optional
from pydantic import Field
from pystratis.core import Model
from pystratis.core.types import Money


class MaxSpendableAmountModel(Model):
    """A MaxSpendableAmountModel."""
    max_spendable_amount: Optional[Money] = Field(alias='maxSpendableAmount')
    fee: Optional[Money] = Field(alias='Fee')
