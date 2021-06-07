from typing import Optional
from pybitcoin import Model
from pybitcoin.types import Money
from pydantic import Field, conint


class UtxoAmountModel(Model):
    """An UtxoAmountModel."""
    amount: Optional[Money] = Field(alias='Amount')
    count: Optional[conint(ge=0)] = Field(alias='Count')
