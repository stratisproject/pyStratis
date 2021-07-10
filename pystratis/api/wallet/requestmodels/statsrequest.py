from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class StatsRequest(Model):
    """A request model for the wallet/wallet-stats endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        min_confirmations (conint(ge=0), optional): Include transaction less this amount from the chain tip. Default=0.
        verbose (bool, optional): If True, give verbose response. Default=True.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    min_confirmations: Optional[conint(ge=0)] = Field(default=0, alias='MinConfirmations')
    verbose: Optional[bool] = Field(default=True, alias='Verbose')
