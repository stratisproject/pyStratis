from pydantic import Field
from pybitcoin import Model


class InfoModel(Model):
    """A InfoModel."""
    cold_wallet_account_exists: bool = Field(alias='coldWalletAccountExists')
    hot_wallet_account_exists: bool = Field(alias='hotWalletAccountExists')
