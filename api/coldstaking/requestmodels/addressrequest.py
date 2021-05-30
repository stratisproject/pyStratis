from typing import Optional
from pydantic import Field
from pybitcoin import Model


class AddressRequest(Model):
    """An AddressRequest."""
    wallet_name: str = Field(alias='walletName')
    is_cold_wallet_address: bool = Field(default=False, alias='isColdWalletAccount')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
