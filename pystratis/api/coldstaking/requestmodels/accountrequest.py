from typing import Optional
from pydantic import Field
from pystratis.api import Model
from pystratis.core import ExtPubKey


# noinspection PyUnresolvedReferences
class AccountRequest(Model):
    """A request model for the coldstaking/cold-staking-account endpoint.

    Args:
        wallet_name (str): The wallet name.
        wallet_password (str): The wallet password.
        is_cold_wallet_account (bool, optional): If this account is for a cold wallet. Default=False.
        extpubkey (ExtPubKey, optional): The extpubkey for the cold wallet.
    """
    wallet_name: str = Field(alias='walletName')
    wallet_password: str = Field(alias='walletPassword')
    is_cold_wallet_account: bool = Field(default=False, alias='isColdWalletAccount')
    extpubkey: Optional[ExtPubKey] = Field(None, alias='extPubKey')
