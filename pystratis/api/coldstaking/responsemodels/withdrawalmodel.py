from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import hexstr


class WithdrawalModel(Model):
    """A WithdrawalModel."""
    transaction_hex: Optional[hexstr] = Field(alias='transactionHex')
