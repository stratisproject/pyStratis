from pydantic import Field
from pybitcoin import Model


class AccountModel(Model):
    """An AccountModel."""
    account_name: str = Field(alias='accountName')
