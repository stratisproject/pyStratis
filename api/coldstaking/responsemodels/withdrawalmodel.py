from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class WithdrawalModel(Model):
    """A WithdrawalModel."""
    transaction_hex: Optional[uint256] = Field(alias='transactionHex')
