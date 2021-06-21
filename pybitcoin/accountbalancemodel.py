from typing import List, Optional
from pydantic import BaseModel, Field
from pybitcoin.types import Money
from .addressmodel import AddressModel
from .cointype import CoinType


class AccountBalanceModel(BaseModel):
    """An AccountBalanceModel"""
    account_name: Optional[str] = Field(alias='accountName')
    account_hd_path: Optional[str] = Field(alias='accountHdPath')
    coin_type: CoinType = Field(alias='coinType')
    amount_confirmed: Money = Field(alias='amountConfirmed')
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    spendable_amount: Money = Field(alias='spendableAmount')
    addresses: Optional[List[AddressModel]]

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
