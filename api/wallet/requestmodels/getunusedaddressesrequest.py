from typing import Optional
from pydantic import Field
from pybitcoin import Model


class GetUnusedAddressesRequest(Model):
    """A GetUnusedAddressesRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    count: str = Field(alias='Count')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
