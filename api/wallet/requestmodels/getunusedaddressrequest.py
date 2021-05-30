from typing import Optional
from pydantic import Field
from pybitcoin import Model


class GetUnusedAddressRequest(Model):
    """A GetUnusedAddressRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
