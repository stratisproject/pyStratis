from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import hexstr


class WithdrawalModel(Model):
    """A WithdrawalModel."""
    transaction_hex: Optional[hexstr] = Field(alias='transactionHex')
