from typing import Optional
from pydantic import Field
from pystratis.api import Model


# noinspection PyUnresolvedReferences
class AddressRequest(Model):
    """A request model for the coldstaking/cold-staking-address endpoint.

    Args:
        wallet_name (str): The wallet name.
        is_cold_wallet_address (bool, optional): If this address is for a cold wallet. Default=False.
        segwit (bool, optional): If this is a segwit address. Default=False.

    """
    wallet_name: str = Field(alias='WalletName')
    is_cold_wallet_address: bool = Field(default=False, alias='IsColdWalletAddress')
    segwit: Optional[bool] = Field(default=False, alias='Segwit')
