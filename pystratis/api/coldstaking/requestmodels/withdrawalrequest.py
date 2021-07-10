from typing import Optional
from pydantic import SecretStr, Field
from pystratis.api import Model
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class WithdrawalRequest(Model):
    """A request model for the coldstaking/cold-staking-withdrawal and coldstaking/endpoint.

    Args:
        receiving_address (Address): The receiving address.
        wallet_password (str): The wallet password.
        wallet_name (str): The wallet name.
        amount (Money): The amount to withdraw to the receiving address.
        fees (Money, optional): The amount paid in fees.
        subtract_fee_from_amount (bool, optional): If fee should be subtracted from amount. Default=True.
    """
    receiving_address: Address = Field(alias='receivingAddress')
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    amount: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    fees: Optional[Money]
