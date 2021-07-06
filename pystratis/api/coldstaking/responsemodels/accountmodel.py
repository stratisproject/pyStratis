from pydantic import Field
from pystratis.api import Model


class AccountModel(Model):
    """A pydantic model for a cold staking account."""
    account_name: str = Field(alias='accountName')
    """The cold staking account name."""
