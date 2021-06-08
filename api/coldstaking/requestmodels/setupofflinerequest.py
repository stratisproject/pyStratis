from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import Address, Money


class SetupOfflineRequest(Model):
    """A SetupOfflineRequest."""
    cold_wallet_address: Address = Field(alias='coldWalletAddress')
    hot_wallet_address: Address = Field(alias='hotWalletAddress')
    wallet_name: str = Field(alias='walletName')
    wallet_account: str = Field(alias='walletAccount')
    amount: Money
    fees: str
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    split_count: Optional[conint(ge=0)] = Field(default=None, alias='splitCount')
    segwit_change_address: Optional[bool] = Field(default=False, alias='segwitChangeAddress')
