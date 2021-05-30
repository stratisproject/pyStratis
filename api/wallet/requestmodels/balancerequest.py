from typing import Optional
from pydantic import Field
from pybitcoin import Model


class BalanceRequest(Model):
    """A BalanceRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    include_balance_by_address: Optional[bool] = Field(default=False, alias='IncludeBalanceByAddress')
