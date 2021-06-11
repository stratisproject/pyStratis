from typing import Optional
from pydantic import Field
from pybitcoin import Model


class AddressRequest(Model):
    """An AddressRequest."""
    wallet_name: str = Field(alias='WalletName')
    is_cold_wallet_address: bool = Field(default=False, alias='IsColdWalletAddress')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
