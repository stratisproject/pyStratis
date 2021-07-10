from typing import Optional
from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class GetAddressesRequest(Model):
    """A request model for the wallet/addresses endpoint.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
        segwit (bool, optional): If True, gets a segwit address. Default=False.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
