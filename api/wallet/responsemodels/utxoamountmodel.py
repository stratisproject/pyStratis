from pybitcoin import Model
from pybitcoin.types import Money
from pydantic import Field, conint


class UtxoAmountModel(Model):
    """An UtxoAmountModel."""
    amount: Money = Field(alias='Amount')
    count: conint(ge=0) = Field(alias='Count')
