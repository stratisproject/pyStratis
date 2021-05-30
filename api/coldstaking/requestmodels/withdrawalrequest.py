from typing import Optional
from pydantic import SecretStr, Field
from pybitcoin import Address, Model
from pybitcoin.types import Money


class WithdrawalRequest(Model):
    """A WithdrawalRequest."""
    wallet_password: SecretStr = Field(alias='walletPassword')
    fees: Money
    receiving_address: Address = Field(alias='receivingAddress')
    wallet_name: str = Field(alias='walletName')
    amount: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
