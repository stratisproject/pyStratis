from pydantic import Field
from pybitcoin import Model


class BalancesRequest(Model):
    """A BalancesRequest."""
    wallet_name: str = Field(alias='walletName')
