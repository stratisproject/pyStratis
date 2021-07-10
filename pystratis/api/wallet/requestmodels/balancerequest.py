from typing import Optional
from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class BalanceRequest(Model):
    """A request model for the wallet/balance endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        include_balance_by_address (bool, optional): If True, includes detailed information about balances by address. Default=False.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    include_balance_by_address: Optional[bool] = Field(default=False, alias='IncludeBalanceByAddress')
