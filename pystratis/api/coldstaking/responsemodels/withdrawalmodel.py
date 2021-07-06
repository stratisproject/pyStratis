from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


class WithdrawalModel(Model):
    """A pydantic model for a cold staking withdrawal transaction."""
    transaction_hex: hexstr = Field(alias='transactionHex')
    """A hex serialized cold staking wallet withdrawal transaction."""
