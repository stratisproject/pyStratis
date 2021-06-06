from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class GetNewAddressesRequest(Model):
    """A GetNewAddressesRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    count: conint(ge=1) = Field(alias='Count')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
