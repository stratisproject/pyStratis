from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Money


class MaxSpendableAmountModel(Model):
    """A MaxSpendableAmountModel."""
    max_spendable_amount: Money = Field(alias='MaxSpendableAmount')
    fee: Money = Field(alias='Fee')
