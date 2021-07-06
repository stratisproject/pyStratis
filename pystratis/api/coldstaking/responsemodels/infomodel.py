from pydantic import Field
from pystratis.api import Model


class InfoModel(Model):
    """A pydantic model for cold wallet information."""
    cold_wallet_account_exists: bool = Field(alias='coldWalletAccountExists')
    """True if cold wallet account exists."""
    hot_wallet_account_exists: bool = Field(alias='hotWalletAccountExists')
    """True if hot wallet account exists."""
