from pydantic import Field
from pybitcoin import Model


class RemoveWalletRequest(Model):
    """A RemoveWalletRequest."""
    wallet_name: str = Field(alias='WalletName')
