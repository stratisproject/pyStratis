from pydantic import Field, BaseModel
from pybitcoin.types import Address, Money
from .cointype import CoinType


class AddressBalanceModel(BaseModel):
    """An AddressBalanceModel."""
    address: Address
    coin_type: CoinType = Field(alias='coinType')
    amount_confirmed: Money = Field(alias='amountConfirmed')
    amount_unconfirmed: Money = Field(alias='amountUnconfirmed')
    spendable_amount: Money = Field(alias='spendableAmount')

    class Config:
        json_encoders = {
            Money: lambda v: v.to_coin_unit(),
        }
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super().json(exclude_none=True, by_alias=True)
