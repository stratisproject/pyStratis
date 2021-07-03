from typing import Optional
from pydantic import Field
from pystratis.core import Model


class AccountModel(Model):
    """An AccountModel."""
    account_name: Optional[str] = Field(alias='accountName')
