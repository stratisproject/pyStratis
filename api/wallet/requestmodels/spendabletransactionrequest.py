from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model


class SpendableTransactionsRequest(Model):
    """A request model for the wallet/spendable-transactions endpoint.

    Args:
        wallet_name: str = Field(alias='WalletName')
        account_name: Optional[str] = Field(default='account 0', alias='AccountName')
        min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='MinConfirmations')
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='MinConfirmations')
