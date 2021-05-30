from pydantic import Field
from pybitcoin import Model


class GetAccountsRequest(Model):
    """A GetAccountsRequest."""
    wallet_name: str = Field(alias='WalletName')
