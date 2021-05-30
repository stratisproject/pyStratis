from pydantic import Field
from pybitcoin import Model


class InfoRequest(Model):
    """An InfoRequest."""
    wallet_name: str = Field(alias='WalletName')
