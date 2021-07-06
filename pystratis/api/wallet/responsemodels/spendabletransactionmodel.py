from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money, uint256
from datetime import datetime


class SpendableTransactionModel(Model):
    """A pydantic model representing spendable transactions."""
    transaction_id: uint256 = Field(alias='id')
    """The transaction hash with spendable output."""
    index: int
    """The index of the spendable output."""
    address: Address
    """The address holding the spendable output."""
    is_change: bool = Field(alias='isChange')
    """If true, address is a change address."""
    amount: Money
    """The amount in the unspent output."""
    creation_time: datetime = Field(alias='creationTime')
    """The output creation time."""
    confirmations: int
    """The number of confirmations for three output."""
