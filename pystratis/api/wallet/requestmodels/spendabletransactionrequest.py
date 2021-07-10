from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class SpendableTransactionsRequest(Model):
    """A request model for the wallet/spendable-transactions endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        min_confirmations (conint(ge=0), optional): Get spendable transactions less this value from chain tip. Default=0.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='MinConfirmations')
