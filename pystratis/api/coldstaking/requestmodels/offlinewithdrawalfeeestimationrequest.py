from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class OfflineWithdrawalFeeEstimationRequest(Model):
    """A request model for the coldstaking/estimate-offline-cold-staking-withdrawal-tx-fee endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str): The account name.
        receiving_address (Address): The receiving address.
        amount (Money): The amount to withdraw to the receiving address.
        subtract_fee_from_amount (bool, optional): If fee should be subtracted from amount. Default=True.
    """
    wallet_name: str = Field(alias='walletName')
    account_name: str = Field(alias='accountName')
    receiving_address: Address = Field(alias='receivingAddress')
    amount: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
