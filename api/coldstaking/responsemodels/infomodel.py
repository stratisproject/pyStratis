from typing import Optional
from pydantic import Field
from pybitcoin import Model


class InfoModel(Model):
    """A InfoModel."""
    cold_wallet_account_exists: Optional[bool] = Field(alias='coldWalletAccountExists')
    hot_wallet_account_exists: Optional[bool] = Field(alias='hotWalletAccountExists')
