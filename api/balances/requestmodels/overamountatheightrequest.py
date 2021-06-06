from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import Money


class OverAmountAtHeightRequest(Model):
    """An OverAmountAtHeightRequest."""
    block_height: conint(ge=0) = Field(alias='blockHeight')
    amount: Money

    def __eq__(self, other) -> bool:
        if self.amount == other.amount and self.block_height == other.block_height:
            return True
        return False
