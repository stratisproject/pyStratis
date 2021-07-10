from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Money


# noinspection PyUnresolvedReferences
class OverAmountAtHeightRequest(Model):
    """A request model for the balances over-amount-at-height endpoint.

    Args:
        block_height (conint(ge=0)): The specified chain height.
        amount (Money): The specified amount, in coin units.
    """
    block_height: conint(ge=0) = Field(alias='blockHeight')
    amount: Money

    def __eq__(self, other) -> bool:
        if self.amount == other.amount and self.block_height == other.block_height:
            return True
        return False
