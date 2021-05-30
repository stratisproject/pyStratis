from typing import Optional
from pydantic import Field
from pybitcoin import Model


class AccountRequest(Model):
    """An AccountRequest."""
    wallet_name: str = Field(alias='walletName')
    wallet_password: str = Field(alias='walletPassword')
    is_cold_wallet_account: bool = Field(default=False, alias='isColdWalletAccount')
    ext_pubkey: Optional[str] = Field(None, alias='extPubKey')
