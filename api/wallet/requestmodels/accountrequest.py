from typing import Optional
from pydantic import Field
from pybitcoin import Model


class AccountRequest(Model):
    """An AccountRequest"""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
