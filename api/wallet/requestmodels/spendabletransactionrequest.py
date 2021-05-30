from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class SpendableTransactionsRequest(Model):
    """A SpendableTransactionsRequest."""
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='MinConfirmations')
