from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class StatsRequest(Model):
    """A StatsRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='MinConfirmations')
    verbose: Optional[bool] = Field(default=True, alias='Verbose')
