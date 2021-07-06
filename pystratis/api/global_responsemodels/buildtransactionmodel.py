from pydantic import Field
from pystratis.core.types import Money, uint256, hexstr
from pystratis.api import Model


class BuildTransactionModel(Model):
    """A pydantic model for a built transaction."""
    fee: Money = Field(default=0)
    """The transaction fee."""
    hex: hexstr
    """The transaction hex."""
    transaction_id: uint256 = Field(alias='transactionId')
    """The transaction hash."""
