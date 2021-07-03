from typing import Optional
from pystratis.api import Model
from pystratis.core.types import Money
from pydantic import Field, conint


class UtxoAmountModel(Model):
    """An UtxoAmountModel."""
    amount: Optional[Money] = Field(alias='Amount')
    count: Optional[conint(ge=0)] = Field(alias='Count')
