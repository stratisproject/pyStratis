from typing import Optional
from pydantic import Field
from pybitcoin import Model


class ExtPubKeyRequest(Model):
    """A request model for the wallet/extpubkey endpoint.

    Args:
        wallet_name: str = Field(alias='WalletName')
        account_name: Optional[str] = Field(default='account 0', alias='AccountName')
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
