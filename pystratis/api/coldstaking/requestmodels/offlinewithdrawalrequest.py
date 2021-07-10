from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class OfflineWithdrawalRequest(Model):
    """A request model for the coldstaking/offline-cold-staking-withdrawal endpoint.

    Args:
        receiving_address (Address): The receiving address.
        wallet_name (str): The wallet name.
        account_name (str): The account name.
        amount (Money): The amount to withdraw to the receiving address.
        fees (Money): The amount paid in fees.
        subtract_fee_from_amount (bool, optional): If fee should be subtracted from amount. Default=True.
    """
    receiving_address: Address = Field(alias='receivingAddress')
    wallet_name: str = Field(alias='walletName')
    account_name: str = Field(alias='accountName')
    amount: Money
    fees: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
