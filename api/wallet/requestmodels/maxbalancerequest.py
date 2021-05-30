from typing import Optional
from pydantic import Field
from pybitcoin import Model


class MaxBalanceRequest(Model):
    """A MaxBalanceRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    fee_type: str = Field(alias='FeeType')
    allow_unconfirmed: Optional[bool] = Field(default=False, alias='AllowUnconfirmed')
