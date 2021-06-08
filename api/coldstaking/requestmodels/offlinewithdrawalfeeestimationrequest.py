from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address, Money


class OfflineWithdrawalFeeEstimationRequest(Model):
    """An OfflineWithdrawalFeeEstimationRequest."""
    wallet_name: str = Field(alias='walletName')
    account_name: str = Field(alias='accountName')
    receiving_address: Address = Field(alias='receivingAddress')
    amount: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
