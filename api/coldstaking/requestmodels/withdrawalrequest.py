from typing import Optional
from pydantic import SecretStr, Field
from pybitcoin import Model
from pybitcoin.types import Address, Money


class WithdrawalRequest(Model):
    """A WithdrawalRequest."""
    receiving_address: Address = Field(alias='receivingAddress')
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(alias='accountName')
    amount: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    fees: Optional[str]
