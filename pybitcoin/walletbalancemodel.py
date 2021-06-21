from typing import List
from pydantic import BaseModel
from .accountbalancemodel import AccountBalanceModel


class WalletBalanceModel(BaseModel):
    """A WalletBalanceModel."""
    balances: List[AccountBalanceModel]

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
