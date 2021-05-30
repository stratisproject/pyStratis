from pydantic import Field, SecretStr
from pybitcoin import Model


class GetUnusedAccountRequest(Model):
    """A GetUnusedAccountRequest."""
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
