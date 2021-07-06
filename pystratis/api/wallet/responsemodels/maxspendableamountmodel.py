from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Money


class MaxSpendableAmountModel(Model):
    """A pydantic model for the maximum spendable amount."""
    max_spendable_amount: Money = Field(alias='maxSpendableAmount')
    """The maximum spendable amount."""
    fee: Money = Field(alias='Fee')
    """The to spend the maximum amount."""
