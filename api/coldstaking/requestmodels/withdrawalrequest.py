from typing import Optional
from pydantic import SecretStr, Field
from pybitcoin import Model
from pybitcoin.types import Address, Money


class WithdrawalRequest(Model):
    """A request model for the coldstaking/cold-staking-withdrawal and coldstaking/endpoint.

    Args:
        receiving_address (Address): The receiving address.
        wallet_password (str): The wallet password.
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        amount (Money): The amount to withdraw to the receiving address.
        fees (Money, optional): The amount paid in fees.
        subtract_fee_from_amount (bool, optional): If fee should be subtracted from amount. Default=True.
    """
    receiving_address: Address = Field(alias='receivingAddress')
    wallet_password: SecretStr = Field(alias='walletPassword')
    wallet_name: str = Field(alias='walletName')
    account_name: Optional[str] = Field(alias='accountName', default='account 0')
    amount: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    fees: Optional[Money]
