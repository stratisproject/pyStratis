from pydantic import Field, conint
from pybitcoin import Address, Model
from pybitcoin.types import Money, uint256


class SpendableTransactionModel(Model):
    """A SpendableTransactionModel."""
    transaction_id: uint256 = Field(alias='id')
    index: conint(ge=0)
    address: Address
    is_change: bool = Field(alias='isChange')
    amount: Money
    creation_time: str = Field(alias='creationTime')
    confirmations: conint(ge=0)
