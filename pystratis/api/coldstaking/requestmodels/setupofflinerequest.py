from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.core.types import Address, Money


# noinspection PyUnresolvedReferences
class SetupOfflineRequest(Model):
    """A request model for the coldstaking/setup-offline-cold-staking and coldstaking/estimate-offline-cold-staking-setup-tx-fee endpoints.

    Args:
        cold_wallet_address (Address): The cold wallet address.
        hot_wallet_address (Address): The hot wallet address.
        wallet_name (str): The wallet name.
        wallet_account (str): The wallet account.
        amount (Money): The amount to send to the old wallet.
        fees (Money): The transaction fee.
        subtract_fee_from_amount (bool, optional): If fee should be subtracted from amount. Default=True.
        split_count (int, optional): Number of transactions to split over. Default=1.
        segwit_change_address (bool, optional): If change address is a segwit address. Default=False.
    """
    cold_wallet_address: Address = Field(alias='coldWalletAddress')
    hot_wallet_address: Address = Field(alias='hotWalletAddress')
    wallet_name: str = Field(alias='walletName')
    wallet_account: str = Field(alias='walletAccount')
    amount: Money
    fees: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    split_count: Optional[conint(ge=1)] = Field(default=1, alias='splitCount')
    segwit_change_address: Optional[bool] = Field(default=False, alias='segwitChangeAddress')
